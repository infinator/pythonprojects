from itertools import permutations  
from PyDictionary import PyDictionary

d = PyDictionary()

w = input("Enter word : ")

print()

seq = permutations(w)
li = list(seq)
strs = [''.join(i) for i in li]
strs = list(dict.fromkeys(strs))

lgth = len(strs)
a_word_mins = 0.021
x = lgth * a_word_mins
mins = int(x)
secs = round(round(x - int(x), 2) * 60)
fhrs = mins / 60
thrs = int(fhrs)
tmins = round(round(fhrs - int(fhrs), 2) * 60)
if mins <= 60:
    print("It may take", mins, "minutes and", secs, "seconds to unscramble the word", "'" + w + "'")
elif thrs <= 24:
    print("It may take", thrs, "hours and", tmins + 5, "minutes to unscramble the word", "'" + w + "'")
else:
    print("This may take days to unscramble such a big word like", "'" + w + "'")
    
print()

print("Checking all", lgth, "comibinations of words...")

l=[]
for a in strs:
	dm = d.meaning(a, disable_errors=True)
	if bool(dm) == True:
		print(strs.index(a) + 1 , "of", lgth,":", a, "makes sense $$$$$")
		l.append(a)
	else:
		print(strs.index(a) + 1 , "of", lgth,":",a, "×" * 3)
size = len(l)
if size > 0:
	print("List of words which make sense : ")
	for j in l:
		print((l.index(j) + 1), ".", j)
		print("Meaning of", j, ": ")
		mean = d.meaning(j)
		if "Noun" in mean:
			print("Noun : ", mean["Noun"][0])
		if "Verb" in mean:
			print("Verb : ", mean["Verb"][0])
		if "Adjective" in mean:
			print("Adjective : ", mean["Adjective"][0])
else:
	print("No word formulated")