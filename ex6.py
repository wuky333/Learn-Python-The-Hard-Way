x = "There are %d types of people."% 10#对文中的变量赋值10
binary = "binary"#赋值
do_not = "don't"#赋值
y = "Those who know %s and those who %s."% (binary,do_not)#赋值

print (x)#显示x，其中赋值10
print (y)#显示y，并把binary和do_not显示

hilarious = False#赋值
joke_evaluation = "Isn't that joke so funny?!%r"#变量赋值，其中%r赋予原始数据

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print (w+e)