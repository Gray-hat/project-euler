#program that finds the sum of all the multiples of 3 or 5 below 1000.


#get all numbers divisible by 3
store = []
below = 1000

for i in range(0, below):
	if (i%3==0 or i%5==0):
		store.append(i)

total = sum(store)

print "The sum of all multiples of 3 or 5 below %d is %d"%(below, total)


def arithmetic_progression(numbers,upper_bound):
    '''Given an list of numbers the function gets the sum of their
        multiples in the range provided'''
            total = 0
                if isinstance(numbers,list):
                for number in numbers:
                    number_terms = (upper_bound/number) if upper_bound > number else 0
                        temp = (number_terms/2.0)* (2 * number + ((number_terms -1) * number))
                        total += temp
                
    return total	
        return False

print "The sum is", arithmetic_progression([3,5],999)