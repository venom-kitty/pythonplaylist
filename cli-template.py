# Welcome to the official CLI template!

import pyfiglet
import ctypes
import platform
import subprocess

os = platform.system()


ctypes.windll.kernel32.SetConsoleTitleW(f'CLI Template') # <--- Replace 'CLI Template' With whatever you want it to be called


def getcmd():
    
    runcmd(input('\nCLI Template>> ')) # <--- Replace 'CLI Template' With whatever you want it to be called


def runcmd(command):

    if command == "customcmd": # <--- Here you can add custom commands, as long as it is above the "subprocess.run(command, shell=True)" line
        print('You ran a custom command!') # <--- Here you can add whatever the command does
    
    else:
        print()
        subprocess.run(command, shell=True)

    getcmd()

banner = pyfiglet.figlet_format('CLI Template') # <--- Replace 'CLI Template' With whatever you want it to be called


print(banner)
print('='*120)

getcmd()
