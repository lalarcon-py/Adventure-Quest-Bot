import os
import pyautogui
import time
from multiprocessing import Process


def main():
    pyautogui.FAILSAFE = True
    #Timer
    print("Starting", end='')
    for i in range(0,5):
        print(".", end='')
        time.sleep(1)

    print('\nGo')
    #Variables
    Skill4 = pyautogui.locateOnScreen('Skill4.png', confidence=0.7)
    Skill3 = pyautogui.locateOnScreen('Skill3.png', confidence=0.7)
    Skill2 = pyautogui.locateOnScreen('Skill2.png', confidence=0.7)
    Death = pyautogui.locateOnScreen('DeathScrren.png', confidence=0.6)
    In_Combat = pyautogui.locateOnScreen('In_Combat.png', confidence=1)
    HP = pyautogui.locateOnScreen('HP.png', confidence=0.2)
    Mana = pyautogui.locateOnScreen('Mana.png', confidence=1)
    Rest = pyautogui.locateOnScreen('Rest.png', confidence=1)

    #Move
    pyautogui.leftClick()
    time.sleep(1)

    #Leveling Script
    while Death == None:
        if Skill4 != None:
            pyautogui.press('4')
        time.sleep(2)
        if Skill3 != None:
            pyautogui.press('3')
        time.sleep(2)
        if Skill2 != None:
            pyautogui.press('2')
        time.sleep(2)
    if Death != None:
        time.sleep(15)

    print("Done.")

def healing():
    In_Combat = pyautogui.locateOnScreen('In_Combat.png', confidence=0.5)
    HP = pyautogui.locateOnScreen('HP.png', confidence=0.2)
    Mana = pyautogui.locateOnScreen('Mana.png', confidence=1)
    Rest = pyautogui.locateOnScreen('Rest.png', confidence=1)

    while In_Combat != None:
        time.sleep(10)
        pyautogui.typewrite('/rest')
        pyautogui.press('Enter')
        time.sleep(10)
processes = []
for i in range(os.cpu_count()):
    print('Registering process')
    processes.append(Process(target=main))

for process in processes:
    processes.start()

for process in processes:
    processes.join()
if __name__ == "__main__":
    main()
