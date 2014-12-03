#a program to calculate sum of even numbers 
#in a fibonnaci sequence

def fibonacci(lower, upper, limit = 0, even_sum = 0):
	'''A program to calculate fibonacci numbers 
	not beyond a certain limit'''

	total = lower + upper
	if total <= limit:
		if total % 2 == 0:
			even_sum += total
		return fibonacci(upper,total,limit, even_sum)
	return "The sum of all even fib numbers to is %d"%even_sum

print fibonacci(0,1,4000000)	