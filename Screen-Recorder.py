import cv2
import pyautogui as p #provides functionalities for programmatically controlling the mouse and keyboard, screen interaction
import numpy as np #used, as pyautogui keeps taking screenshots of the screen for screen recording and saves them in an array hence numpy used

# Find resolution of your screen
res = p.size()

# Filename in which to store the recording
fn = input("Enter the file name and path: ")

# Set frame rate, how fast how slow. high frame rate means fast ie more frames per second 
fps = 25.0

# FourCC codec for video writing
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Create video writer object
#will write frame to video file
output = cv2.VideoWriter(fn, fourcc, fps, res)

# Create recording window
cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording", (600, 400))

# Main recording loop
try:
    while True:
        img = p.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB 
        #changin into rgb as opencv reads in bgr while computer saves in rgb  
        #No Conversion Needed: If you're using imshow(), you can display the frame directly without conversion. 
        #Use Conversion: If you're using libraries that expect RGB input, then convert the frame using cv2.cvtColor().

        # Write frame to video file
        output.write(frame)

        # Display frame in the window
        cv2.imshow("Live_Recording", frame)

        # Check for exit key (q)
        if cv2.waitKey(1) == ord("q"):
            break

finally:
    # Release resources
    output.release()
    cv2.destroyAllWindows()
    
    
    """ 
    try-finally Block: The try block contains the code that might raise exceptions, such as errors during video frame capture or writing. The finally block is executed regardless of whether an exception occurs, ensuring that the output.release() line is always executed, even if an error happens.
    output.release(): This line closes the video writer, saving the final video file and releasing the associated resources. Placing it within the finally block guarantees its execution, preventing incomplete or corrupted files.
    """

    #C:\Users\Shweta Tyagi\Computer Vision Project outputs\Screen_Recording.mp4
    