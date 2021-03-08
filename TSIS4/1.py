import re

file = open('raw.txt',encoding="utf8")
text = file.read()

BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NamePattern = r"\nФилиал.*(?P<Name>\b[A-Z]+)"

BINText = re.search(BINPattern, text).group("BIN")
NameText = re.search(NamePattern, text).group("Name")

print(NameText)
print(BINText)


itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)


for m in re.finditer(itemPattern, text):
    print(m.group("name") + "\n" + " " + m.group("count")+ "\n" + m.group("price") + "\n"+ m.group("total1"))
TimePattern = r"\nВремя: (?P<Time>\b[0-9].*\n{1}(?P<Address>.*))"
TimeText = re.search(TimePattern, text).group("Time")
AddressText = re.search(TimePattern, text).group("Address")
print(TimeText)
file.close()