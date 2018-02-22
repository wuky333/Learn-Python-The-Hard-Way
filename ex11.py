print ("How old are you?",end="")#不换行的操作方式
age = input()#python 3 中，对raw_input（）合并到input（）
print ("How tall are you?",end="")
height = input()
print ("How much do you weight?",end="")
weight = input()

print ("So you're %r old,%r tall and %r heavy."%(
        age,height,weight))