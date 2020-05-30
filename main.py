import requests
import filecmp
import os.path
from sys import argv
from os import system
from time import sleep

def main():
    url = 'https://emis.freeuni.edu.ge/index.php?mode=info&sub=nishnebi&lang=ka'
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    cookies = {'userType': 'student', 'userName': '+', 'userid:': '20326'} 

    phpsessid = argv[1]
    cookies['PHPSESSID'] = phpsessid

    with requests.Session() as s:
        r = s.get(url, headers=headers, cookies=cookies)

        if not os.path.exists('old'):
            print('getting first sample')
            with open('old', 'w') as f:
                f.write(r.text)
            wait()

        while True:
            print('getting new sample')
            r = s.get(url, headers=headers, cookies=cookies)
            print('response:', r)

            with open('new', 'w') as f:
                f.write(r.text)

            if changed():
                print('website content changed!')
                break

            system('mv new old')
            wait()

def changed():
    return not filecmp.cmp('old', 'new', shallow=False) 

def wait():
    sleep(10)

if __name__ == '__main__':
    main()

