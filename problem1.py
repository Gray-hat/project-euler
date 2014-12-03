#program that finds the sum of all the multiples of 3 or 5 below 1000.


#get all numbers divisible by 3
store = []
below = 1000

for i in range(0, below):
	if (i%3==0 or i%5==0):
		store.append(i)

total = sum(store)

print "The sum of all multiples of 3 or 5 below %d is %d"%(below, total)	