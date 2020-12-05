import requests
from lxml import etree
import parsel

url = 'http://ehall.xianyangzhiyuan.cn/xsfw/sys/jbxxapp/*default/index.do?t_s=1601990773281&amp_sec_version_=1&gid_=YjZlTjlveW15Y3oxQkVRZDJ0Q0RjZ0o3VGU0SVBMYy9YeWdPaDVKQWJXMjJEejd5VFc3V2FoWGdBblFkY0Z1OEpPNC9sUnY1Q2tHSUpxblZPcS9NUmc9PQ&EMAP_LANG=zh&THEME=indigo#/wdxx'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
data = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie": "route=efe5121545d83dd7406ab6ee4f19e0b7; EMAP_LANG=zh; THEME=indigo; _WEU=OdhC01qPZHFzgWzTyk1GPkGIm_lLs5*ryFGfC4K409XJpxZbMkSHs1geRaUcHV36s8OFjxQruTAiBoKSyOidqZj9NiDS4a1q4vddFgnJ5olcWm4VatMtbM1yhXQgtViVBAWvZeUAdaz6qtDobhOCVnmBZ1m0R*fB2iAaELZVrSeLkaMNk39Y49BCBGNRIKDv; Hm_lvt_87ff160709018bdf47c98d4598a9c6cb=1601990472; Hm_lpvt_87ff160709018bdf47c98d4598a9c6cb=1601990498; JSESSIONID=xev-E4hd628K8zzc-yooZUwUzsoPxNJaWstC18cX5wjClXdz8QX_!-2114671599; amp.locale=zh_CN; MOD_AUTH_CAS=MOD_AUTH_ST-951881-1hFYbHmAKvp3Qy1m7mag1601990590976-BHdp-cas; asessionid=7d1afcf5-979b-4cdc-ba2d-17e985572705"
}
html = requests.get(url=url, headers=headers, data=data).text

print(html)
