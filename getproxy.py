import json
import time
import datetime
import requests
import re
res1 = dict()
res2 = list()
class Downloadproxies():
    def __init__(self) -> None:
        self.api = {
    'socks4':[
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxyscan.io/download?type=socks4",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
        "https://api.openproxylist.xyz/socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://www.freeproxychecker.com/result/socks4_proxies.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
        'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt',
        'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt',
        'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt',
        'https://openproxy.space/list/socks4'],
    'socks5': [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://www.proxyscan.io/download?type=socks5",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://api.openproxylist.xyz/socks5.txt",
        "https://www.freeproxychecker.com/result/socks5_proxies.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
        'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks5.txt',
        'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
        'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt',
        'https://openproxy.space/list/socks5',
        'https://spys.me/socks.txt'],
    'http': [
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxyscan.io/download?type=http",
        "http://spys.me/proxy.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://api.openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
        "http://alexa.lr2b.com/proxylist.txt",
        "http://rootjazz.com/proxies/proxies.txt",
        "https://www.freeproxychecker.com/result/http_proxies.txt",
        r"http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt"
        "https://proxy-spider.com/api/proxies.example.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
        "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
        'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
        'https://openproxy.space/list/http'
    ]}
        self.proxy_dict = {'socks4':'','socks5':'','http':''}
        pass

    def get(self,type):
        self.proxy_list = []
        for api in self.api[type]:
            try:
                self.r = requests.get(api,timeout=5)
                if self.r.status_code == requests.codes.ok :
                    self.proxy_list += re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}',self.r.text)
                    self.proxy_dict[type] = list(set(self.proxy_list))
            except:
                pass
        if type == 'socks4':
            try:
                r = requests.get("https://www.socks-proxy.net/",timeout=5)
                self.part = str(r.text)
                self.part = self.part.split("<tbody>")
                self.part = self.part[1].split("</tbody>")
                self.part = self.part[0].split("<tr><td>")
                self.proxies = ""
                for proxy in self.part:
                    proxy = proxy.split("</td><td>")
                    try:
                        if self.proxies != '':
                            self.proxies=self.proxies + proxy[0] + ":" + proxy[1] + "\n"
                    except:
                        pass
                if self.proxies != '':
                    self.proxy_list += self.proxies.split('\n')
                self.proxy_list = list(set(self.proxy_list))
                self.proxy_dict[type] = list(set(self.proxy_list))
            except:
                pass
        print('> Get {} proxies done'.format(type))

    def get_extra(self):
        self.yesterday = datetime.date.today() + datetime.timedelta(-1)
        self.r = requests.get('https://checkerproxy.net/api/archive/{}-{}-{}'.format(self.yesterday.year,self.yesterday.month,self.yesterday.day))
        if self.r.text != '[]': 
            self.json_result = json.loads(self.r.text)
        else:
            del self.r
            self.t_d_b_yesterday = datetime.date.today() + datetime.timedelta(-2)
            self.r = requests.get('https://checkerproxy.net/api/archive/{}-{}-{}'.format(self.t_d_b_yesterday.year,self.t_d_b_yesterday.month,self.yesterdat_d_b_yesterday.day))
            self.json_result = json.loads(self.r.text)
        for i in self.json_result:
            if i['type'] == 1 and i['ip'] != '172.23.0.1':
                self.proxy_dict['http'].append(i['addr'])
            if i['type'] == 2 and i['ip'] != '172.23.0.1':
                self.proxy_dict['http'].append(i['addr'])
            if i['type'] == 4:
                self.proxy_dict['socks5'].append(i['addr'])
        print('> Get extra proxies done')

    def get_all(self):
        self.get('socks4')
        self.get('socks5')
        self.get('http')
        self.get_extra()

    def save(self,typ):
        global res1,res2
        tmp = list()
        self.out_file = r"C:\Python310\files\proxy.txt"
        for i in self.proxy_dict[typ]:
            if '#' in i or i == '\n':
                self.proxy_dict[typ].remove(i)
            else:
                tmp.append(i)
                res2.append(i)
        if typ == 'socks4':
            res1.update({'socks4':tmp})
        elif typ == 'socks5':
            res1.update({'socks5':tmp})
        elif typ == 'http':
            res1.update({'https':tmp})
            f = open(self.out_file,'w')
            f.write(str(res1)+'\n')
            f.write(str(res2))
            f.close()
        print("> Have already downloaded proxies list as "+self.out_file)

    def save_all(self):
        self.save('socks4')
        self.save('socks5')
        self.save('http')

if __name__ == '__main__':
    d = Downloadproxies()
    d.get_all()
    d.save_all()