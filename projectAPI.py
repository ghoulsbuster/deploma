import codecs

file = codecs.open("test.mpp", encoding="utf-8", errors="ignore")

text = file.read()
print(text)
