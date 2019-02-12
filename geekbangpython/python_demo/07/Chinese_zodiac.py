chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#
# print(chinese_zodiac[-1])
#
# print(chinese_zodiac[0:4])

year = 1989
print(year % 12)
print(chinese_zodiac[year % 12])

print ('狗' not in chinese_zodiac)
print (chinese_zodiac + chinese_zodiac)
print(chinese_zodiac + 'adb')
print(chinese_zodiac * 3)

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
            u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (12, 27)

zodiac_day = filter(lambda x: x <= (month,day), zodiac_days)
zodiac_day_len = len(list(zodiac_day)) % 12
print(zodiac_day_len)
print(zodiac_name[zodiac_day_len])
