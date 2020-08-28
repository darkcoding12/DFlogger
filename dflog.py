import os
intro = """

\033[01m\033[31m  ____  _ _  \033[01m _                              
\033[01m\033[31m |  _ \|  _| \033[01m| |     __    ___   ___  __  ____
\033[01m\033[31m | | | | |_  \033[01m| |   / _ \ / _  |/ _  |/ _ \ '__| 
\033[01m\033[31m | |_| |  _| \033[01m| |__| (_) | (_| | (_| |  __/ |    
\033[01m\033[31m |____/|_|   \033[01m|____|\___/ \__, |\__, |\___|_|    
                         \033[01m|___/ |___/            
\033[0m
         .:Coding-Lab:.  t.me\cod1ng_lab
                 version 1.0.1 
"""
os.system('clear')
print(intro)
print('''
[\033[32m1\033[0m] \033[34mIP Logger\033[0m
[\033[32m2\033[0m] \033[34mEXIT\033[0m
''')
num = input('[+] : ')
if num == '1':
  port = input("[PORT] : ")
  os.system('php -S localhost:' + port)
if num == '2':
  os.system('exit()')
