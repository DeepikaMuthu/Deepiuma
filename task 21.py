def merge(list1, list2): 

      

    merged_list = tuple(zip(list1, list2))  

    return merged_list 

      
# Driver code 

list1 = [1, 2, 3] 

list2 = ['a', 'b', 'c'] 

print(merge(list1, list2)) 


numbers = [6, 9, 3, 1]
numbers_sorted = sorted(numbers)
numbers_sorted


numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def even_numbers(num):
    if(num%2 == 0):
        return True
    else:
        return False

evenNums = filter(even_numbers, numbers)
print('Even Numbers are:')
for num in evenNums:
    print(num)