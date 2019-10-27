import pyautogui
import keyboard
import os

path = './resources'

def initializeNumberButtonList():
    numberButtonList = []
    numberButtonList.append(f'{path}/button0.png')
    numberButtonList.append(f'{path}/button1.png')
    numberButtonList.append(f'{path}/button2.png')
    numberButtonList.append(f'{path}/button3.png')
    numberButtonList.append(f'{path}/button4.png')
    numberButtonList.append(f'{path}/button5.png')
    numberButtonList.append(f'{path}/button6.png')
    numberButtonList.append(f'{path}/button7.png')
    numberButtonList.append(f'{path}/button8.png')
    numberButtonList.append(f'{path}/button9.png')
    return numberButtonList

def clickButton(fileName):
    button = pyautogui.locateOnScreen(fileName)
    pyautogui.click(button.left, button.top)

if __name__ == '__main__':
    # locate window original point
    windowOriginalPoint = pyautogui.locateOnScreen(f'{path}/logo.png')

    numberButtonList = initializeNumberButtonList()

    call = f'{path}/call.png'
    clear = f'{path}/clear.png'

    # extension
    # extension = '11003'

    # make calls
    # for eachNumber in extension:
    #     clickButton(numberButtonList[int(eachNumber)])
    #     pyautogui.PAUSE = 1.5
    # clickButton(call)

    fastDial = f'{path}/fastDial.png'
    group = f'{path}/11901.png'

    print('started')

    while True:
        if keyboard.is_pressed('f10'):
            print("pressed")
            try:
                clickButton(fastDial)
            except:
                pass
            clickButton(group)
            break
        else:
            print("waiting")
            pass

    os.system("start EXCEL.EXE file.xlsx")
