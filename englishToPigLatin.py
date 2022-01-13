import time

start_time = time.time()

li=input("Write a sentence : ").split(" ")
print()
print("Pig Latin version : ")
el=""
pl=""
for i in li:
	if i[0] not in "aeiou":
		ln=len(i)
		ll=i[ln-1]
		st=""
		for j in range(1,ln):
			st+=i[j]
		st+=i[0]+"ay"
		pl+=st+" "
	else:
		st=i+"yay"
		pl+=st+" "
print(pl)

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")