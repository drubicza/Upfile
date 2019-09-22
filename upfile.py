import os
import re
import requests

def Upfile():
    R = requests.post('http://fs3.upfile.mobi:2052/upload_1', files={'file': (Nm, Fl, 'text/javascript')}, allow_redirects=True).text
    if 'upload_success' in R:
        r = re.findall('<div><a href = "(.+?)"/>http://upfile.mobi/', R)[0]
        print(('\x1b[0;92m[\x1b[0m+\x1b[0;92m]\x1b[0m Link \x1b[0;93mDownload \x1b[0mFile : \x1b[0;92m%s\n\x1b[0m=============================' % r))
    else:
        print('\x1b[0;91m[!]\x1b[0m Gagal Upload File : \x1b[0;93m{} \x1b[0m'.format(Fl))
    print('\x1b[0m=============================')


print('\x1b[0m=============================')
os.system('figlet -f digital "Uploads Upfile"')
print('\x1b[0m=============================')
try:
    Nm = input('\x1b[0;92m[\x1b[0m+\x1b[0;92m]\x1b[0m File Upload : ')
    Fl = open(Nm).read()
    print('\x1b[0m=============================')
except FileNotFoundError:
    exit(('\x1b[0;91m[!] \x1b[0mFile \x1b[0;93m' + Nm + ' \x1b[0m Tidak Ada'))

Upfile()
