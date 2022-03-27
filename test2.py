"""
 * Project name(项目名称)：Python枚举类
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 21:23
 * Version(版本): 1.0
 * Description(描述)： 
 """
from enum import Enum

if __name__ == '__main__':
    # 创建一个枚举类
    Color = Enum("Color", ('red', 'green', 'blue'))

    print(Color.red)
    print(Color['red'])
    print(Color(1))
    print(Color.green)
    print(Color['green'])
    print(Color(2))
    print(Color.blue)
    print(Color['blue'])
    print(Color(3))

    print(Color.red.name)
    print(Color.red.value)
    print(Color['red'].name)
    print(Color['red'].value)
    print(Color(1).name)
    print(Color(1).value)

    print(Color.green.name)
    print(Color.green.value)
    print(Color['green'].name)
    print(Color['green'].value)
    print(Color(2).name)
    print(Color(2).value)

    print(Color.blue.name)
    print(Color.blue.value)
    print(Color['blue'].name)
    print(Color['blue'].value)
    print(Color(3).name)
    print(Color(3).value)

    for color in Color:
        print(color)

    for color in Color:
        print(color.name)

    for color in Color:
        print(color.value)

    print(Color.red == Color.green)
    print(Color.red.name is Color.green.name)

    for name, value in Color.__members__.items():
        print(name, "---->", value)

    for value in Color.__members__.values():
        print(value)

    for name in Color.__members__.keys():
        print(name)
