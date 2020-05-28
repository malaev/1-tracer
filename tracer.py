import subprocess
import re
import urllib.request
import json


def getInfoByIp(ip):
    url = "https://ipinfo.io/" + ip + "/json"
    getInfo = ''
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        getInfo = ''
    infoList = json.load(getInfo)

    country = ''
    org = ''
    try:
        country = infoList['country']
    except:
        country = ''
    try:
        org = infoList['org']
    except:
        org = ''
    return  [country, org]

print('Введите доменное имя или ip адрес')
domen = input()
args = ["tracert", domen]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = str(process.communicate()[0])
lines = re.findall(r'[A-Za-z0-9.-]+ \[\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b\]', data)
lines = [elem.strip(r'\[|\]') for elem in lines]
index = 1
for elem in lines[1:]:
    ipInfo = getInfoByIp(elem.split(' [')[1])
    print(str(index) + ' ' + elem.split(' [')[0] + ' ' + elem.split(' [')[1] + ' ' + ipInfo[0] + ' ' + ipInfo[1])
    index += 1
