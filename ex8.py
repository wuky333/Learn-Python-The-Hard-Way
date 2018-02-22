formatter = "%r %r %r %r"

print (formatter %(1,2,3,4))
print (formatter %("one","two","three","four"))
print (formatter %("一","二","三","四"))
print (formatter %(True,False,False,True))
print (formatter %(formatter,formatter,formatter,formatter))
print (formatter %(
                    "I had this thing.",
					"That you could type up right.",
					"But it didn't sing.",#有单引号的时候显示双引号
					"So I said goodnight."
					)
		)			