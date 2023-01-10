#!python

from os import link
import pyautogui as pg
import pyperclip as pp

def shortcutKey(type,key):
    # pg.sleep(0.1)
    pg.keyDown(type)
    pg.press(key)
    pg.keyUp(type)
    # pg.sleep(0.1)

def nextTab():
    shortcutKey('ctrl','tab')
    pg.sleep(0.1)
    # pg.sleep(0.5)

def writefile(data):
    with open('links copied.txt','a') as file:
        file.write(data+'\n')

def sitescopied():
    with open('links copied.txt','r') as file:
        return file.read().split()

def main_copy():
    if __import__('os').path.exists('links copied.txt'):
        with open('links copied (old).txt','w') as old:
            with open('links copied.txt','r') as file:
                old.write(file.read())
    with open('links copied.txt','w') as file:
        file.write("")
    for i in range(6):
        print(f"[-] starting in {5-i}",end='\r')
        pg.sleep(1)
    position = pg.position()
    while True:
        pg.click(position)
        shortcutKey('ctrl','a')
        shortcutKey('ctrl','c')
        if a:=pp.paste() in sitescopied():
            break
        writefile(pp.paste())
        nextTab()

def main_run():
    chromeOpen = lambda link:__import__('os').system(f'start chrome "{link}"')
    with open('links copied.txt','r') as file:
        links = file.read().split()
    for link in links:
        # print(f"[.] opening : {link} ...")
        chromeOpen(link)

if __name__ == "__main__":
    print("[!] currently this script only works in Windows")
    print("[+] Do you want to Copy links (1) or run links (2)?")
    type = input('[+] PRESS 1 OR 2 >> ')
    if type.strip() not in ['1','2']: exit()

    if type.strip()=='2':
        print('[+] Opening Links in Chrome...')
        main_run()
    elif type.strip()=='1':
        print("[+] now just go the Chrome windows where all the sites are running")
        print("    and just click on the url link.")
        pg.sleep(2)
        print("[+] Copying site links...")
        main_copy()
        print("[+] file saved >> 'links.copied.txt'")
        print("[+] previous data (if any) backup >> 'links copied (old).txt'")
    input("[+] PROGRAM COMPLETED!")