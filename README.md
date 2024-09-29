# Screen Recorder Using PyAutoGUI and OpenCV

## Overview:
This project implements a screen recording tool that captures the screen in real-time using PyAutoGUI and records the screen frames as a video using OpenCV. Users can specify the file path, frame rate, and resolution to create high-quality screen recordings. The tool is perfect for creating tutorial videos, presentations, or capturing live screen activity. The code is well-commented for clarity.

## Features:
- Records screen activities in real-time.
- Allows users to specify the file name and save location for the video.
- Customize the frame rate to control the speed and smoothness of the recording.
- Creates a resizable live recording window for monitoring the screen capture.
- Fully commented code to guide users through each step of the implementation.

## Technologies Used:
- **Python**: Core programming language.
- **PyAutoGUI**: Used to capture screenshots of the screen.
- **OpenCV**: Used for processing and writing frames into a video file.
- **NumPy**: Efficient array manipulation for handling screenshot data.

## How to Use:

### Requirements:
- Python 3.x
- Required Python libraries:
    - `opencv-python`
    - `pyautogui`
    - `numpy`

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Screen-Recorder.git
   cd Screen-Recorder
   ```
2. Install the required dependencies:
   ```bash
   pip install opencv-python pyautogui numpy
   ```

### Usage:
1. Run the script:
   ```bash
   python screen_recorder.py
   ```

2. When prompted:
   - Enter the file name and path where you want to save the recording (e.g., `C:\Users\YourUsername\Videos\Screen_Recording.mp4`).

3. The screen recording will start, and a window will appear to display the live recording. The recording will continue until you press the **'q'** key.

4. The video will be saved in the specified location once the recording is complete.

### Example:
```bash
Enter the file name and path: C:\Users\YourUsername\Videos\Screen_Recording.avi
```

The script will create and save the screen recording in the specified location, displaying a live preview of the recording in a resizable window.

---

## Contributing:
Feel free to contribute by submitting pull requests or reporting issues.




