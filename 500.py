import requests, os, time, sys
html = 'https://pastebin.com/raw/zR1FQh80'
html2 = 'https://pastebin.com/raw/5iNiUd8n'
try:
    Pro = requests.get(html).text
    Coder = requests.get(html2).text
except:
    print('\x1b[1;39m» \x1b[1;31mFail In Your Internet')
    exit('\x1b[1;39m')
else:
    print('\x1b[1;39m[+] \x1b[1;34mGet the password from here \x1b[1;32m»» ', Coder )
    print()
    pwd = input('\x1b[1;99m»» \x1b[1;32mEnter Password \x1b[1;34m:\x1b[1;39m ')
    if pwd == Pro:
        print('\n\x1b[1;39m» \x1b[1;39m[√] \x1b[1;34mDone Login\n\n')
        time.sleep(1)
        os.system('clear')
    else:
        print(' \n\x1b[1;39m[x] \x1b[1;31mPassword is wrong\n  \n\x1b[1;39m»» \x1b[1;32mGo to the Telegram channel to find the password\n\x1b[1;39m»» \x1b[1;34mTelegram: https://t.me/CoderPro1')
        exit('\x1b[1;39m')
    n = '\x1b[0;32m########## Welcome To Script YourFreedom ##########\n\n\x1b[1;34mTelegram: https://t.me/CoderPro1\n'
for c in n:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.03)
else:
    print('\x1b[0;32m')
    log = """
  _____   _____   _____   _____   _____   
/  ___| /  _  \ |  _  \ | ____| |  _  \  
| |     | | | | | | | | | |__   | |_| |  
| |     | | | | | | | | |  __|  |  _  /  
| |___  | |_| | | |_| | | |___  | | \ \  
\_____| \_____/ |_____/ |_____| |_|  \_\ 
 _____   _____    _____  
|  _  \ |  _  \  /  _  \ 
| |_| | | |_| |  | | | | 
|  ___/ |  _  /  | | | | 
| |     | | \ \  | |_| | 
|_|     |_|  \_\ \_____/ 

"""
    for c in log:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0009)
    else:
        x = """
\033[1;34m########## By / CoderPRO ##########
\033[1;34m######## Script YourFreedom ########

"""
        for w in x:
            sys.stdout.write(w)
            sys.stdout.flush()
            time.sleep(0.05)
time.sleep(0.4)



try:
	count = int(input('\x1b[1;39m»» \x1b[1;32mNumber of accounts \x1b[1;34m:\x1b[1;39m '))
except:
	print()
	print('\x1b[1;39m[×] \x1b[1;31mwrong entry')
	exit('\x1b[1;39m')
print()
for nazer  in range(0, count):
    ln = 'abcdefghijklmnopqrstuvwxyz1234567890'
    import requests, random, time, sys
    
    from requests.structures import CaseInsensitiveDict
    h = 'a'
    j = 'p'
    i = 'h'
    l = 'i'
    url = 'https://www.your-freedom.net/' + h + j + l + '.' + j + i + j
    headers = CaseInsensitiveDict()
    headers['Content-Length'] = '247'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['Host'] = 'www.your-freedom.net'
    headers['Connection'] = 'Keep-Alive'
    
    ussser = 'Coder_' + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln)
    passs = 'Pro_' + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln) + random.choice(ln)
    
    naaame = random.choice(['Coder','Pro','Pro'])
    passst = random.choice(['Coder','Pro','Pro'])
    data = 'cmd=create_account&data={"username":"ussser","password":"passs","email":"ussser@gmail.com","first_name":"naaame","last_name":"passst","no_verification":true}'.replace('ussser', ussser).replace('passs', passs).replace('naaame', naaame).replace('passst', passst)
  
    
    try:
        maganyatt = requests.post(url, headers=headers, data=data).text
        if 'Account created' in maganyatt:
            file1 = open('CoderPro_Freedom.txt', 'a')

            file1.write('username : ' + ussser + '\n' + 'password : ' + passs + '\n' + '~~~~~~~~~~~~~~~~~~~~~' + '\n')
            file1.close()
            
            n = '\x1b[1;34mWait\x1b[1;39m .............\n\n'
            for c in n:
            	sys.stdout.write(c)
            	sys.stdout.flush()
            	time.sleep(0.05)
            	
            time.sleep(2)
            print('\x1b[1;32mDone Created Account')
            
            print('\x1b[1;32mDone Saved Account in \x1b[1;39m»\x1b[1;34m CoderPro_Freedom.txt\n')
            
            print('~~~~~~~~~~~~~~~~~~~~')
            print('\x1b[1;39m')

        else:
            print('\x1b[1;31mErorr')
            
    except:
        print('\x1b[1;39m» \x1b[1;31mFail In Your Internet')
        exit('\x1b[1;39m')
        
