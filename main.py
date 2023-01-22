import time, pyautogui
time.sleep(5)

def get_passwords():
    with open('mypasswords.txt', 'r') as file:
        passwords = file.readlines()
        passwords = [password.strip() for password in passwords]
        passwords = set(passwords)
        passwords = list(passwords)
        return passwords

def reconnect():
    time.sleep(0.5)
    pyautogui.moveTo(469, 402, 2, pyautogui.easeInQuad)
    pyautogui.click()
    pyautogui.moveTo(460, 505, 2, pyautogui.easeInQuad)
    pyautogui.click()
    pyautogui.moveTo(458, 431, 2, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(4)

if __name__ == "__main__":
    passwords = get_passwords()
    for i in range(len(passwords)):
        print(i)
        pyautogui.press("/")
        time.sleep(0.25)
        pyautogui.typewrite("login " + passwords[i])
        time.sleep(0.4)
        pyautogui.press("enter")
        time.sleep(0.5)
        if ((i % 15 == 0) or (i % 18 == 0)) and (i != 0):
            reconnect()
            continue
