import argparse
parser = argparse.ArgumentParser()

#参考连接：https://docs.python.org/zh-cn/3/howto/argparse.html
#https://docs.python.org/3/howto/argparse.html
#https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse
#关于固定参数

"""
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args)
print(args.echo)
"""

"""
parser.add_argument("square", help="display a square of a given number", type=int)
#那是因为 argparse 会把我们传递给它的选项视作为字符串，除非我们告诉它别这样。所以，让我们来通过type=int告诉 argparse 来把这一输入视为整数：
args = parser.parse_args()
print(args)
print(args.square**2)
"""

#关于可选参数
parser.add_argument("-v","--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity: #如果指定verbosity，则显示下面这句话
    print("verbosity turned on")

#不添加这一选项时程序没有提示任何错误而退出，表明这一选项确实是可选的。
# 注意，如果一个可选参数没有被使用时，相关变量被赋值为 None，在此例中是 args.verbosity，这也就是为什么它在 if 语句中被当作逻辑假。

#短提示
