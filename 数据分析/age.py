# coding = utf-8
with open('day.txt', 'r') as fp:
    day = fp.read()
    x = 20020409
    num = 0
    for nwe_day in day:
        print(nwe_day)
        if nwe_day == x:
            num += 1
            print(1)

    print(num)