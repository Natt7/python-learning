x = 'xyz'
if x == 'abc' :
    print(x)
elif x =='xyz' :
    print('x = xyz')
else:
    print('x no equal')

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

print(chinese_zodiac[-1])
print(chinese_zodiac[0:4])

year = int(input('请输入您的出生年份：'))
print(year % 12)
print(chinese_zodiac[year % 12])

if (chinese_zodiac[year % 12]) == '狗' :
    print('狗年运势。。。')