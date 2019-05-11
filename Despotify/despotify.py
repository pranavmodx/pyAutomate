# A small python script for muting the speaker when an annoying audio ad starts to play in Spotify's Desktop App and resuming once the ad ends.

import time
import pyautogui


def openSpotify():
    pyautogui.hotkey('command', 'space')
    pyautogui.typewrite('spotify app')
    time.sleep(1)
    pyautogui.press('enter')


def locateIcon(icon):
    try:
        img = pyautogui.locateOnScreen(f'{icon}', greyscale=True)
        return img
    except TypeError:
        pass


def clickSpeaker(sX, sY):
    pyautogui.click(x=sX, y=sY)


# Driver Code
openSpotify()

playTime = locateIcon('ad.png')
if playTime is None:
    playTime = locateIcon('ad2.png')
    if playTime is not None:
        try:
            sX, sY = locateIcon('speakerBtn.png')
            clickSpeaker(sX, sY)
            time.sleep(30)
            openSpotify()
            clickSpeaker(sX, sY)

        except TypeError:
            print('Speaker button out of range')
    else:
        print('No ads are playing')
