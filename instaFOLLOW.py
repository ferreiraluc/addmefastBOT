import pyautogui as pt 
from time import sleep  
import webbrowser as web 
from pynput.mouse import Button, Controller 

contador = 2 

urL='https://addmefast.com'

chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
web.register('chrome', None, web.BackgroundBrowser(chrome_path))
web.get('chrome').open(urL)
sleep(6)


class Addmefast:

        def __init__(self, speed=.3, click_speed=.3):
            self.speed = speed
            self.click_speed = click_speed


        def FacebookLikes(self):
            while contador < 100:
                like = pt.locateOnScreen('likeADD.png', confidence=.7)
                if (like != None):
                    try:
                        pt.moveTo(like[0:5], duration=self.speed)
                        pt.leftClick()
                        sleep(8)
                    except: 
                        print('likeADD error')
                else:
                    position1 = pt.locateOnScreen('reference1.png', confidence=.7)
                    pt.moveTo(position1[0:5], duration=self.speed)
                    pt.moveRel(0, 290, duration=self.speed)
                    pt.leftClick()
                    sleep(6)
                    if (position1 == None):
                        print('bugou')

                likeinsta = pt.locateOnScreen('seguir.png', confidence=.7)
                if (likeinsta != None):
                    try:
                        pt.moveTo(likeinsta[0:5], duration=self.speed)
                        pt.leftClick()
                        sleep(3)
                        pt.leftClick(670, 21, duration=self.click_speed)
                    except:
                        print('likeinsta nao encontrado')
                else:
                    pt.leftClick(670, 21, duration=self.click_speed)
                
                errorbutton = pt.locateOnScreen('errorbutton.png', confidence=.7)
                if (errorbutton == None):
                    print('loaderror not FIND')
                else:
                    pt.moveTo(errorbutton[0:5], duration=self.speed)
                    pt.leftClick()
                    sleep(4)
                    

wa = Addmefast(speed=.3, click_speed=.3)
wa.FacebookLikes()
