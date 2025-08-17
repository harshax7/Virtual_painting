A real-time virtual painting app using your webcam and OpenCV. Track colored objects and draw on the screen like using a magic brush — without touching the screen!

📌 Features

🎯 Real-time color detection using HSV color space.

🎨 Multiple color tracking (easily customizable).

🖼 Draw on screen with any colored object.

✏ Smooth contour detection for accurate tracking.

🔄 Works with live webcam feed.

📂 Workflow
flowchart LR
    A[Webcam Feed] --> B[Convert to HSV Color Space]
    B --> C[Apply Color Mask]
    C --> D[Find Contours & Object Center]
    D --> E[Draw Points on Canvas]

📂 How It Works

Color Ranges – Predefined HSV values detect specific colors.

Masking – Filters out everything except the selected color.

Contours – Finds object center for precise tracking.

Drawing – Points are stored and continuously drawn on the frame.

🛠 Requirements

Python 3.x

OpenCV

NumPy

Install dependencies:

pip install opencv-python numpy

▶ Usage

Run the script:

python virtual_paint.py


Move a colored object in front of the webcam.

Draw in the air — your strokes appear on the screen.

Press Q to quit.

🎯 Example Output
Color Detection	Drawing Output

	
📜 License

This project is open-source and available under the MIT License.
