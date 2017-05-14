#Create 10 functions using lambda, map, reduce, filter, list comprehension and generator
#one simple use example included for each function


# 4 basic operations functions using "map"
#to be potentially applied to 2 numbers lists of equal length

#add pairs of values from 2 lists
list1 = [1,2,3,4,5]
list2 = [4,6,7,8,9]
def addition(first, second):
    return map(lambda x, y: x+y, first, second)
    
test1 = addition(list1, list2)
print test1


#subtract the value from the second list from the one in the same position in the first list
list1 = [1,2,3,4,5]
list2 = [4,6,7,8,9]
def subtraction(first, second):
    return map(lambda x, y: x-y, first, second)

test2 = subtraction(list1, list2)
print test2


#multiply pairs of values from 2 lists
list1 = [1,2,3,4,5]
list2 = [4,6,7,8,9]    
def multiplication(first, second):
    return map(lambda x, y: x*y, first, second)
    
test3 = multiplication(list1, list2)
print test3    


#divide pairs of values from 2 lists (exception in case the value from the second list equals zero)
list1 = [1,2,3,4,5]
list2 = [4,6,7,0,9]  
def division(first, second):
    return map(lambda x, y: x/float(y) if y!=0 else "undefined", first, second)
    
test4 = division(list1, list2)
print test4 
  
  
  
#filter can be applied to... filter out desired values from a list
#checking for odd numbers from a number list
number_list = [1,2,4,5,6,7,66,77,88,99]
result = filter(lambda x: x % 2 == 1, number_list)
print result

#checking for even numbers from a number list
number_list = [1,2,4,5,6,7,66,77,88,99]
result = filter(lambda x: x % 2 == 0, number_list)
print result



#reduce can be used to reduce the values on a list to a single value
#find max number

maxTo100 = reduce(lambda a,b: a if (a>b) else b, range(1, 101))
print maxTo100


#find min number
number_list = [1,2,4,5,6,7,66,77,88,99]

min_number_list = reduce(lambda a,b: a if (a<b) else b, number_list)
print min_number_list



#list comprehension

pyth = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print pyth



#generator 
def pythagorean(n):
    for x in range(1,n):
        for y in range(x,n):
            for z in range(y,n):
                if x**2 + y **2 == z**2:
                    yield (x,y,z)
                    
p =  pythagorean(100)
for x in p:
    print x,
print
