# MouseHelper 🖱️ [Demonstration >>>](https://github.com/Dhivyno/MouseHelper/blob/main/Mouse%20Helper%20Demonstration.mp4)

This is a camera-controlled mouse program that helps disabled people access the features of a mouse without using the traditional version. The program uses OpenCV and Mediapipe to detect various landmarks on a hand and uses the corresponding coordinates to offer moving, clicking and dragging of the mouse. 

---

### Gestures

- **Moving**: Use your index finger to move the mouse around the screen. The index finger is detected as active when its tip's y-coordinate is higher than the joints connecting it to the palm.

- **Clicking**: Use your index finger and thumb to activate the clicking protocol which freezes the mouse in place anticipating a click. This is done by first keeping the thumb below its corresponding joints and raising it above when the cursor is over the element you want to click on. Then, a click is initiated simply when the thumb and index fingers are moved closer than a given threshold (30 pixels). 

- **Dragging**: Use your index and middle finger to activate the dragging protocol. Firstly, bringing the index and middle finger together within the threshold stated above initialises the coordinates from where you intend to drag from. Then, move the cursor using the move function to the coordinates where you intend to stop dragging and simply "click" your index and middle fingers together. This moves the cursor from your initial point to your final point while holding down left click which enables the dragging action. (A time.sleep(0.5) function is provided to avoid double initialising and preventing the mouse from dragging between 2 distant points).

---



The demonstration starts with showing how the landmarks on the hand are used to move the cursor around the screen. The landmark used for cursor movement is Landmark 8 in the [mediapipe hand landmark model](https://google.github.io/mediapipe/solutions/hands.html). 

Then, it moves onto clicking which is represented by a red circle  🔴 connecting landmark 8 (index tip) and landmark 4 (thumb tip) when they are brought close to each other. This causes the cursor to freeze in place to allow easy and precise locational clicking. When the radii of the landmarks overlap each other, the clicking is enabled and a green circle 🟢 connects the two landmarks. 

After that, the dragging mechanism is shown by a green circle 🟢 connecting landmark 8 (index tip) and landmark 12 (middle tip). When the radii of the landmarks overlap, the start position is set and the circle is switched to blue 🔵 to indicate that the stop position has to be selected. When the radii overlap once again, the stop position is set and the cursor moves from the start position to the stop position with a constant speed. This allows the user to be able to select specific areas of the screen like text.

---

### Required modules

- Mediapipe

- OpenCV-python

- AutoPy    (***WARNING***: AutoPy seems to install only in python 3.8.10, I have tried it in 3.10.4 but an error is thrown which is not related to pip so I presume it's a legacy dir problem)

- Time

- Numpy
