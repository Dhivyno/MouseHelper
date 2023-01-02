import cv2
import numpy as np
import Functions as htm
import time
import autopy

camera_width, camera_height = 640, 480
frame_rate = 30
smoothening = 7
prev_time = 0
prev_x, prev_y = 0, 0
current_x, current_y = 0, 0
drag = False
cap = cv2.VideoCapture(0)
cap.set(3, camera_width)
cap.set(4, camera_height)
detector = htm.Detector(hands_max=1)
screen_width, screen_height = autopy.screen.size()

while True:
    success, img = cap.read()
    img = detector.find(img)
    landmark_list, bbox = detector.findPos(img, 0, True)
    if len(landmark_list) != 0:
        x_index, y_index = landmark_list[8][1:]
        x_middle, y_middle = landmark_list[12][1:]

    finger_tips = detector.finger_tips_active()
    if finger_tips[1] == 1 and finger_tips[0] == 0:
        x3 = np.interp(x_index, (frame_rate, camera_width - frame_rate), (0, screen_width))
        y3 = np.interp(y_index, (frame_rate, camera_height - frame_rate), (0, screen_height))
        current_x = prev_x + (x3 - prev_x) / smoothening
        current_y = prev_y + (y3 - prev_y) / smoothening
        autopy.mouse.move(screen_width - current_x, current_y)
        cv2.circle(img, (x_index, y_index), 15, (255, 0, 255))
        prev_x, prev_y = current_x, current_y

    if finger_tips[1] == 1 and finger_tips[0] == 1:
        length, img, coords = detector.findDis(4, 8, img)
        if length < 40:
            cv2.circle(img, (coords[4], coords[5]), 15, (0, 255, 0), cv2.FILLED)
            autopy.mouse.click()
        else:
            cv2.circle(img, (coords[4], coords[5]), 15, (0, 0, 255), cv2.FILLED)

    if finger_tips[1] == 1 and finger_tips[2] == 1:
        length, img, coords = detector.findDis(8, 12, img)
        if not drag:
            if length < 30:
                drag = True
                x_drag, y_drag = screen_width - current_x, current_y
                time.sleep(0.5)
            cv2.circle(img, (coords[4], coords[5]), 15, (0, 255, 0), cv2.FILLED)
        elif drag:
            if length < 30:
                drag = False
                autopy.mouse.move(x_drag, y_drag)
                autopy.mouse.toggle(down=True)
                autopy.mouse.smooth_move(screen_width - current_x, current_y)
                autopy.mouse.toggle(down=False)
            cv2.circle(img, (coords[4], coords[5]), 15, (255, 0, 0), cv2.FILLED)


    current_time = time.time()
    prev_time = current_time
    cv2.imshow("Image", img)
    cv2.waitKey(1)
