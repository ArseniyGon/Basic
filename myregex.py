import re
txt1 = "This_one_sentence."
x = re.sub("_", " ", txt1)
print(x)

txt2 = "This_shows_count_of_replacements."
y = re.sub("_", " ", txt2, 2)
print(y)

txt3 = "This is a test search sentence."
a = re.search("a", txt3)
print(a)
