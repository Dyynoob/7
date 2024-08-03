import os
import sys
import time

def script():
    print("Starting script...")
    os.system("yes | sudo pacman -S neofetch")
    os.system("yes | sudo pacman -S wget")
    os.system("yes | sudo pacman -S grub")
    os.system("yes | sudo pacman -S os-prober")


    os.system("sudo wget -O /etc/issue https://numberseven.xyz/DBL/cfg/issue")
    os.system("sudo wget -O /usr/bin/neofetch https://numberseven.xyz/DBL/cfg/neofetch")
    os.system("sudo wget -O /etc/default/grub https://numberseven.xyz/DBL/cfg/grub")
    os.system("sudo wget -O /home/wallpaper.jpg https://numberseven.xyz/DBL/extra/wallpaper.jpg")   
    os.system("sudo wget -O /usr/local/bin/pookie https://numberseven.xyz/DBL/extra/pookie")      
    os.system("sudo mkdir /pookie")        
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
    print("\n\n\n\n")
    hostnamechange = input("change hostname? (y/n): ")
    if hostnamechange.startswith("y"):
        os.system("sudo hostnamectl set-hostname WaifuMachine")
        os.system("sudo wget -O /etc/hostname https://numberseven.xyz/DBL/cfg/hostname")      
    else:
        print("Host name will not be changed.\n\n\n")
        
    print("\n\n\nA wallpaper has been put /home. \nFeel free to set your wallpaper to that if you are feeling extra pathetic.\n\n\n")
    print("-- -- -- -- -- -- -- -- --")
    print("\n\nInstallation has succeeded... Please restart your computer.\n\n\n")
    

if not os.getenv("SUDO_USER"):
    print("\n\n\nThis script must be ran using sudo. Try sudo ./setup\n\n\n")

else:


    print("\n\n\n")


    print("This script requires a desktop environment and Grub.")
    input("THE OPERATING SYSTEM MUST BE ARCH LINUX (press enter to continue.)")
    print("\n\n\n")
    
    if not os.path.exists('/boot/grub'):
    
        print("We have found that grub is not found in /boot...")
        time.sleep(1)
        print("Confirmation to continue:", end=" ", flush=True)
        for i in range(3, 0, -1):
            print(f"{i}...", end="", flush=True)
            time.sleep(1)
        print()  # To move to the next line after countdown

        response = input("Continue? (y/n): ")
        if response.startswith("y"):
            script()

    else:
        script()
