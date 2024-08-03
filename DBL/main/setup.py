import os
import sys
import time

def script():
    print("Starting script...")
    os.system("yes | sudo pacman -S neofetch")
    os.system("yes | sudo pacman -S wget")
    os.system("yes | sudo pacman -S grub")
    os.system("yes | sudo pacman -S os-prober")


    os.system("sudo cp ../cfg/issue /etc/issue")
    os.system("sudo cp ../cfg/neofetch /usr/bin/neofetch")
    os.system("sudo cp ../cfg/grub /etc/default/grub")
    os.system("sudo cp ../extra/wallpaper.jpg ~/wallpaper.jpg")    
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
    print("\n\n\n\n")
    hostnamechange = input("change hostname? (y/n): ")
    if hostnamechange.startswith("y"):
        os.system("sudo hostnamectl set-hostname WaifuMachine")
        os.system("sudo cp ../cfg/hostname /etc/hostname")      
    else:
        print("Host name will not be changed.\n\n\n")


if not os.getenv("SUDO_USER"):
    print("This script must be ran using sudo. Try sudo python3 setup.py")

else:


    print("\n\n\n")


    print("This script requires a desktop environment and Grub.")
    input("THE OPERATING SYSTEM MUST BE ARCH LINUX (press enter to continue.)")
    print("\n\n\n")
    
    if os.path.exists('/boot/grub'):
    
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


