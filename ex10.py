tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a\\ cat."

fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#额外练习

while True:#循环语句1，需要加冒号，缩进
     for i in ["/","-","|","\\","|"]:#循环语句2，需要加冒号，缩进
	     print ("%s\r" % i),#按照i的顺序显示