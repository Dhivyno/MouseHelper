import cv2
import mediapipe as mp
import time
import math


class Detector():
    def __init__(self, mode=False, hands_max=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.hands_max = hands_max
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.Hands = mp.solutions.hands
        self.hands = self.Hands.Hands(static_image_mode=self.mode, max_num_hands=self.hands_max, min_detection_confidence=self.detection_confidence, min_tracking_confidence=self.tracking_confidence)
        self.draw = mp.solutions.drawing_utils
        self.tips = [4, 8, 12, 16, 20]

    def find(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(img, hand_landmarks,
                                               self.Hands.HAND_CONNECTIONS)

        return img

    def findPos(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.landmark_list = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.landmark_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)

        return self.landmark_list, bbox

    def finger_tips_active(self):
        finger_tips = []
        try:
            if self.landmark_list[self.tips[0]][2] < self.landmark_list[self.tips[0] - 1][2]-50:
                finger_tips.append(1)
            else:
                finger_tips.append(0)
        except:
            finger_tips.append(0)

        for id in range(1, 5):
            try:
                if self.landmark_list[self.tips[id]][2] < self.landmark_list[self.tips[id] - 2][2]:
                    finger_tips.append(1)
                else:
                    finger_tips.append(0)
            except:
                finger_tips.append(0)


        return finger_tips

    def findDis(self, p1, p2, img, draw=True, r=15, t=3):
        x1, y1 = self.landmark_list[p1][1:]
        x2, y2 = self.landmark_list[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    prev_time = 0
    current_time = 0
    cap = cv2.VideoCapture(0)
    detector = Detector()
    while True:
        success, img = cap.read()
        img = detector.find(img)
        landmark_list, bbox = detector.findPos(img)
        if len(landmark_list) != 0:
            print(landmark_list[4])

        current_time = time.time()
        prev_time = current_time


        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()