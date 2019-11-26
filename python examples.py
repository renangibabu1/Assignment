# import re

# text= "The rain in Spain"
# x = re.search("^The.*Spain$",text)
#
# if x:
#     print("YES! we have a match")
# else:
#     print("No match")

import re

# str = "The rain in spain"
# x = re.findall("ai",str)
# print(x)

str1 = "thi rain in spain"
x = re.search(r'\bs\w+',str1)
# print(x.span())
# print(x.string)
print(x.group())
