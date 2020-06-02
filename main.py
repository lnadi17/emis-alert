import requests
import filecmp
import os.path
from sys import argv
from os import system
from time import sleep
from bs4 import BeautifulSoup as bs

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
                f.write(parse_table(r.text))
            wait()

        while True:
            print('getting new sample')
            r = s.get(url, headers=headers, cookies=cookies)
            print('response:', r)

            with open('new', 'w') as f:
                f.write(parse_table(r.text))

            if changed():
                print('website content changed!')
                system('diff old new > diff')

                name = ''
                with open("name", "r") as f:
                    name = f.read()

                message = ''
                with open("message", "r") as f:
                    message = f.read()
                    message = message.replace('\n', '\\n')
                    message = message.replace('<', '+')
                    message = message.replace('>', '-')

                system("messer --command='m \"" + name[:-1] + "\" " + message + '\'')

            system('mv new old')
            wait()

def changed():
    return not filecmp.cmp('old', 'new', shallow=False) 

def wait():
    sleep(5)

def parse_table(text):
    result = ''
    soup = bs(text, 'lxml')
    for semester_block in soup.findAll("div", {"class": "sem_block"}):
        title = semester_block.find_next("div", {"class": "block_title"})
        result += title.string[0] + ' სემესტრი\n'
        table_body = semester_block.find_next("tbody")
        rows = table_body.find_all("tr", recursive=False)
        for row in rows:
            cols = row.find_all('td', recursive=False)
            #result += row['data-lid'] + ', '
            result += ' '.join(cols[0].string.split()[1:])
            result += ', ' + cols[3].string + ' (' + cols[4].string + ')\n'
    return result

if __name__ == '__main__':
    main()

