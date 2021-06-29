#multiples arguments(x and y):
 x=(lambda x,y:x*5+y*10)(2,5)
 print(x)
 
#Fibonacci series using lambda and map function:By using lambda and map function

def fibonacci(count): 

    fib_list = [0, 1] 

  

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), 

                                         range(2, count))) 

  

    return fib_list[:count] 

  

print(fibonacci(10)) 
 
   
#multiply each number of given list with a given number:
	a_list = [1, 2, 3]

multiplied_list = [element * 2 for element in a_list]

print(multiplied_list)


#Divisible by a from a list of list:
	my_list = [12, 65, 54, 39, 102, 339, 221,]
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)

#count the even numbers in a given list of integers:

list1 = [10, 21, 4, 45, 66, 93, 1] 
even_count, odd_count = 0, 0

for num in list1: 

    if num % 2 == 0: 

        even_count += 1

  else: 

        odd_count += 1
print("Even numbers in the list: ", even_count) 

print("Odd numbers in the list: ", odd_count)