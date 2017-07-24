tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

"""
while True:
    for i in ["/","-","|","\\","|"]:
        print ("%s\r"%i)
"""
for i in ["/","-","|","\\","|"]:
    print ("%s\r"%i)
for i in ["/","-","|","\\","|"]:
    print ("%r\r"%i)


# study drill
"""
使用/s打印出来的结果是：/、-、|、\、|
使用/r打印出来的结果是：'/'、'-'、'|'、'\\'、'|'
"""
