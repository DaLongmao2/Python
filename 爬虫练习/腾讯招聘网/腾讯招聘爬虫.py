import requests

while True:
    try:
        start_page = int(input('开始页数:'))
        end_page = int(input('结束页数：'))
        num = 0
        fp = open('tex.txt', 'w+', encoding='utf-8')
        for page in range(start_page, end_page + 1):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1604591695791&pageIndex={}&pageSize=10'
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
            }
            response = requests.get(url.format(page)).json()['Data']['Posts']
            for info in response:
                num += 1
                print('正在爬去{}'.format(info['PostURL']))
                fp.write("{} {} \n 职位名称：{} \n详情链接: {} \n职位类别：{} \n招聘详情：{} \n工作地点: {} \n发布时间: {} \n".format(
                    num,
                    ' =' * 50,
                    info['RecruitPostName'],
                    info['PostURL'],
                    info['BGName'],
                    info['Responsibility'],
                    info['CountryName'] + info['LocationName'],
                    info['LastUpdateTime']
                ))
        fp.close()
        break
    except ValueError:
        print('请输入一个数字！！！')
