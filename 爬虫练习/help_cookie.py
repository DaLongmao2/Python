# coding = utf-8
from urllib import request, parse
from http.cookiejar import CookieJar

# 不使用 cookie 去请求QQ空间
url = "https://user.qzone.qq.com/3301660640"


def not_cookie():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    req = request.Request(url=url, headers=head)
    resp = request.urlopen(req)
    # print(resp.read().decode('utf-8'))
    # write 写入函数必须写入一个str的数据类型
    # resp.read() 读出来的是一个 bytes 数据类型
    # 解码 bytes -> decode -> str
    # 编码 str -> encode -> bytes
    with open('Qzone.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))
        print('写入完成 - 不使用cookie')


def cookie():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        # 'cookie': 'RK=hK74KTPXcq; ptcz=1fe2eced3310eaec8d087faa3ba897bfdc60a8b3e16e74d87984347c78dfd607; pgv_pvid=9642771656; _qpsvr_localtk=0.8415924109218376; pgv_info=ssid=s206813948; uin=o0872039610; skey=@W1TDPo8ga; p_uin=o0872039610; pt4_token=Kk250B6Uz*1RAptsSvw*pR1xr*Okxly4qx6XH79lweg_; p_skey=0Dv875B4A0z8kIwoXs1KQ7E*2SyxkbwM6OTlWIdxMuM_; Loading=Yes; qz_screen=1920x1080; 872039610_todaycount=0; 872039610_totalcount=17797; QZ_FE_WEBP_SUPPORT=1; qzmusicplayer=qzone_player_872039610_1599468183824; qqmusic_uin=0872039610; qqmusic_key=@W1TDPo8ga; qqmusic_fromtag=6'
        'cookie': 'RK=hK74KTPXcq; ptcz=1fe2eced3310eaec8d087faa3ba897bfdc60a8b3e16e74d87984347c78dfd607; pgv_pvid=9642771656; zzpaneluin=; zzpanelkey=; _qpsvr_localtk=0.5683212192060292; pgv_info=ssid=s4345952128; ptui_loginuin=3149508868; Loading=Yes; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; 3149508868_totalcount=3963; 3149508868_todaycount=0; cpu_performance_v8=5; __Q_w_s__QZN_TodoMsgCnt=1; pgv_pvi=114143232; pgv_si=s2626964480; uin=o3301662640; skey=@ly6QVJnX6; p_uin=o3301662640; pt4_token=E70vf9sVbEslmmgNAxgMzs7Y7ZHlOt71*VprxaPilwI_; p_skey=VH-ELU*pBEgOMOY5z3sclDRg1hf1SH8spnOXggn-GP4_'
    }
    req = request.Request(url=url, headers=head)
    resp = request.urlopen(req)
    # print(resp.read().decode('utf-8'))
    # write 写入函数必须写入一个str的数据类型
    # resp.read() 读出来的是一个 bytes 数据类型
    # 解码 bytes -> decode -> str
    # 编码 str -> encode -> bytes
    with open('Qzone.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))
        print('写入完成 - 使用cookie')


def login_cookie():
    # 1.登陆
    cookiejar = CookieJar()  # 创建CookieJar对象
    hand = request.HTTPCookieProcessor(cookiejar)  # 使用cookiejar创建一个HTTPCookieProcessor 对象
    opener = request.build_opener(hand)  # 使用创建的head创建一个opener
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    data = {
        'name': '3149508868',
        'password': 'gy2876235880ZXY'
    }
    login_url = 'https://user.qzone.qq.com/'
    req = request.Request(url=login_url, headers=headers, data=parse.urlencode(data).encode('utf-8'))
    request.urlopen(req)

    # 访问个人主页
    dapeng_url = 'https://user.qzone.qq.com/872039610'
    resp = opener.open(dapeng_url)
    with open('Qzone.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))
        print('模拟登陆完成')


if __name__ == '__main__':
    # not_cookie()
    cookie()
    # login_cookie()
