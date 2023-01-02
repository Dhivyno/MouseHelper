# MouseHelper

This is a camera-controlled mouse program that helps disabled people access the features of a mouse without using the traditional version. The program uses OpenCV and Mediapipe to detect various landmarks on a hand and uses the corresponding coordinates to offer moving, clicking and dragging of the mouse. 

---

### Gestures

- **Moving**: Use your index finger to move the mouse around the screen. The index finger is detected as active when its tip's y-coordinate is higher than the joints connecting it to the palm.

- **Clicking**: Use your index finger and thumb to activate the clicking protocol which freezes the mouse in place anticipating a click. This is done by first keeping the thumb below its corresponding joints and raising it above when the cursor is over the element you want to click on. Then, a click is initiated simply when the thumb and index fingers are moved closer than a given threshold (30 pixels). 

- **Dragging**: Use your index and middle finger to activate the dragging protocol. Firstly, bringing the index and middle finger together within the threshold stated above initialises the coordinates from where you intend to drag from. Then, move the cursor using the move function to the coordinates where you intend to stop dragging and simply "click" your index and middle fingers together. This moves the cursor from your initial point to your final point while holding down left click which enables the dragging action. (A time.sleep(0.5) function is provided to avoid double initialising and preventing the mouse from dragging between 2 distant points).

---

### Required modules

- Mediapipe

- OpenCV-python

- AutoPy    (***WARNING***: AutoPy seems to install only in python 3.8.10, I have tried it in 3.10.4 but an error is thrown which is not related to pip so I presume it's a legacy dir problem)

- Time

- Numpy
