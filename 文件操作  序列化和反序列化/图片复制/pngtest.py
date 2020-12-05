# coding = utf-8
str_name = "Zombiez-{}.png"
for i in range(32):
    str_name.format(i)
    open(r'str_name', 'wb', encoding='utf-8')