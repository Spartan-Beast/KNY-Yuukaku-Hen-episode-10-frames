import cv2 as cv
from pathlib import Path
import os

# capture video from mp4
parts = ['KNY_part1.mp4', 'KNY_part2.mp4', 'KNY_part3.mp4']
for part in parts:
    video = cv.VideoCapture(part)
    i = 0
    
    cwd = str(Path(__file__).parents[0])
    dir = str(f'{cwd}\KNY_wallpapers')

    while True:
        #read each subsequent frame
        while(video.isOpened()):
            successful_frame_read, frame = video.read()
            if successful_frame_read == True:
                # Save frame by frame into disk using imwrite method
                os.chdir(dir)
                cv.imwrite(f'KNY_WP{str(i)}.jpg', frame)
                i += 1

            # This condition prevents from infinite looping incase video ends.
            else:
                break         
        
            if cv.waitKey(1) & 0Xff == ord('q'):
                break
        
        else:
            break
        
# release the video capture object
video.release()