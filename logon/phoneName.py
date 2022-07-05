import random


def phone():
    second = random.randint(9999999, 100000000)
    first = random.choice([130, 188, 135])
    tel = "{}{}".format(first, second)
    return tel


def company():
    location = random.choice(["余姚市", "宁波市", "浙江省", "南京市", "北京市", "上海市", "江苏省", "南京市", "黄山市", "温州市",
                                 "慈溪市", "广州市", "台州市", "绍兴市", "杭州市", "福建省", "厦门市", "安徽市", "重庆市"])
    s = random.choice("不知道取啥名字就瞎几把乱填的随便整吧")
    d = random.choice("不知道取啥名字就瞎几把乱填的随便整吧")
    end = random.choice(["有限公司", "股份公司", "公司"])
    com = "{}{}{}{}".format(location, s, d, end)
    return com


def name():
    a1 = ['张', '金', '李', '王', '赵']
    a2 = ['玉', '明', '龙', '芳', '军', '玲']
    a3 = ['', '立', '玲', '', '国', '']
    na = random.choice(a1)+random.choice(a2)+random.choice(a3)
    return na

