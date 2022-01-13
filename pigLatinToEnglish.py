#from itertools import permutations 
import time

start_time = time.time()

from PyDictionary import PyDictionary
import collections
inp=input("Enter a pig-latin sentence : ").split(" ")
print("Translating...")
sto=[]
stx=[]
sty=[]
for i in inp:
	if i[-2:]=="ay" and i[-3:]!="yay":
		sto.append(i[-3]+i[:-3])
	elif i[-3:]=="yay":
		stx.append(i[:-4]+i[-4])
		sty.append(i[-3]+i[:-3])
toCheck=stx+sty
d=PyDictionary()
pronouns=["we", "you", "she", "her", "him", "they", "them", "this", "that", "these", "those", "which", "whom", "whose", "whichever", "whoever", "whomever", "myself", "ourselves", "yourself", "yourselves", "himself", "herself", "itself", "themselves", "what", "who", "my", "our", "your", "yours", "his", "hers", "ours", "yours", "theirs"]
for k in toCheck:
	dm=d.meaning(k, disable_errors=True)
	if bool(dm)==True and k!="yis" or k in pronouns:
		sto.append(k)
if len(inp)!=len(sto):
	print("""Your input seems to have multiple translated sentences.
One of the translated sentences is here:""")
	ind=[]
	for q in sto:
		for r in inp:
			if q in r or (q[1:] in r and r[-3]==q[0]):
				ind.append(inp.index(r))
				break
	pair=dict(zip(ind, sto))
	od = collections.OrderedDict(sorted(pair.items()))
	for s,t in od.items():
		print(t, end=" ")
	print()
else:
	print("Translated to English: ")
	ind=[]
	for q in sto:
		for r in inp:
			if q in r or (q[1:] in r and r[-3]==q[0]):
				if inp.index(r) not in ind:
					ind.append(inp.index(r))
					break
				else:
					inp[inp.index(r)]="somethingElse"
					ind.append(inp.index(r))
					break
	pair=dict(zip(ind, sto))
	od = collections.OrderedDict(sorted(pair.items()))
	for s,t in od.items():
		print(t, end=" ")
	print()

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")
			
			
			
			
			
			