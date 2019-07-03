# A small Python script for organizing subtitles in a folder containing movies,
# video lectures and others. It's annoying to disable subtitles every time
# we play a video. This keeps it in a separate folder and prevents automatic loading.

import os
import shutil

for dirpath, dirnames, filenames in os.walk('path_of_folder'):
    dirCreated = 0
    if (len(filenames) != 0):
        for filename in filenames:
            _, isSrtFile = os.path.splitext(filename)
            if (isSrtFile == '.srt'):
                if (os.path.exists(f'{dirpath}/Subtitles') == False and dirCreated == 0):
                    os.mkdir(f'{dirpath}/Subtitles')
                    dirCreated = 1
                shutil.move(f'{dirpath}/{filename}', f'{dirpath}/Subtitles/')
