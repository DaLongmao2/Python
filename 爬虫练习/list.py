# coding = utf-8
# data_list = ['http://www.win4000.com/wallpaper_detail_173092_1.html', 'http://www.win4000.com/wallpaper_detail_173091.html', 'http://www.win4000.com/wallpaper_detail_173090.html', 'http://www.win4000.com/wallpaper_detail_173089.html', 'http://www.win4000.com/wallpaper_detail_173088.html', 'http://www.win4000.com/wallpaper_detail_173087.html', 'http://www.win4000.com/wallpaper_detail_173086.html', 'http://www.win4000.com/wallpaper_detail_173085.html', 'http://www.win4000.com/wallpaper_detail_173084.html', 'http://www.win4000.com/wallpaper_detail_173070.html', 'http://www.win4000.com/wallpaper_detail_173069.html', 'http://www.win4000.com/wallpaper_detail_173059.html', 'http://www.win4000.com/wallpaper_detail_173058.html', 'http://www.win4000.com/wallpaper_detail_173057.html', 'http://www.win4000.com/wallpaper_detail_173056.html', 'http://www.win4000.com/wallpaper_detail_173054.html', 'http://www.win4000.com/wallpaper_detail_173051.html', 'http://www.win4000.com/wallpaper_detail_173050.html', 'http://www.win4000.com/wallpaper_detail_173048.html', 'http://www.win4000.com/wallpaper_detail_173047.html', 'http://www.win4000.com/wallpaper_detail_173046.html', 'http://www.win4000.com/wallpaper_detail_173045.html', 'http://www.win4000.com/wallpaper_detail_173044.html', 'http://www.win4000.com/wallpaper_detail_173043.html', '/zt/youxi.html', '/zt/oumeimeinv.html', '/zt/fengjing_1.html', '/meinvtag38_1.html', '/zt/chuangyi.html']
# data_list2 = [data_list[i:i + 2] for i in range(0, len(data_list), 2)]
# print(data_list2)
# for i in data_list2:
#     print(i[0])
#     print(i[1])


x = 236
year, x2 = 0, 0
while True:
    year += 1
    year, x2 = x2, year
    print(year)
    if x == x2:
        break
