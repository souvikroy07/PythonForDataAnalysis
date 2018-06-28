Dependencies

Please install the following libraries

Folium : pip install folium

Selenium: pip install selenium 

FFmpeg: brew install ffmpeg

Pillow: pip install pillow

Phantom JS: Copy the phantomjs executable within the phantomjs\bin folder and place it in your $PATH.  On a Mac, go to Finder and Press Command+Shift+G and type in /usr/local/bin. Paste the file.

Running the code:
Open the PythonDataAnalysisProject.ipynb file and run all cells. The code will begin saving frames in frames_pickup_NYC_Test and frames_dropoff_NYC_Test.

To view old frames, look inside frames_dropoff_NYC and frames_pickup_NYC.

Once all frames have been generated, navigate to the project folder in terminal and run 

ffmpeg -r 10 -i frames_dropoff_NYC/frame_%05d.png -c:v libx264 -vf fps=5 -crf 17 -pix_fmt yuv420p dropoff_NYC_test.mp4

to generate the drop_off data video and

ffmpeg -r 10 -i frames_pickup_NYC/frame_%05d.png -c:v libx264 -vf fps=5 -crf 17 -pix_fmt yuv420p pickup_NYC_test.mp4

to generate the pickup data video

To combine the two videos into one video, run 

ffmpeg -i dropoff_NYC_test.mp4 -i pickup_NYC_test.mp4 -preset ultrafast -filter_complex vstack combined.mp4

Old videos are already saved in the folder.
