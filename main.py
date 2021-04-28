import pyautogui
import time

def main():

    pyautogui.FAILSAFE = True
    #Timer
    print("Starting", end='')
    for i in range(0,10):
        print(".", end='')
        time.sleep(1)

    print('Go')
    Skill4 = pyautogui.locateOnScreen('Skill4.png')
    Skill3 = pyautogui.locateOnScreen('Skill3.png')
    Skill2 = pyautogui.locateOnScreen('Skill2.png')
    Death = pyautogui.locateOnScreen('DeathScrren.png')
    #Do Something
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.leftClick()
    while True:
        pyautogui.press('4')
        time.sleep(1)
        pyautogui.press('3')
        time.sleep(1)
        pyautogui.press('2')
        time.sleep(1)

    print("Done.")
if __name__ == "__main__":
    main()