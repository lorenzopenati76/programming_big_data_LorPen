# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:00:00 2017

@author: Lorenzo
"""


from calculator import*

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "Welcome to our calculator.\nFind below the options available.\n"
print "+ for sum"
print "- for subtraction"
print "* for multiplication"
print "/ for division"
print "'sqr' for square root"
print "'exp' for exponential"
print "'squ' for square"
print "'cub' for cube"
print "'sin' for sine"
print "'cos' for cosine"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

while True:
    
    op_choice = raw_input("Please select an operation by entering one of the options indicated in the menu above.\nOr enter 'q' to quit.\n")

    if op_choice.lower() == 'q':
	
		print "Quitting.\n"
		break
        
	
    elif op_choice in ('+','-','*','/','exp'):
        
        print "Thank you for choosing an operation.\n"
			
        while True:
				
				num1 = raw_input('Please enter the first (or base) number.\n')
				num2 = raw_input('Please enter the second (or power) number.\n')             
			
				try:
					
					if op_choice == '+':
						
						result = add(num1,num2)
						operation = "sum"
						break

					elif op_choice == '-':
						
						result = subtract(num1,num2)
						operation = "subtraction"
						break

		   
					elif op_choice == '*':
						
						result = multiply(num1,num2)
						operation = "multiplication"
						break

					elif op_choice == '/':
						
						result = divide(num1,num2)
						operation = "division"
						break

					elif op_choice == 'exp':
						
						result = exponential(num1,num2)
						operation = "power"
						break
						  
				except:
					
					print "You need to enter numbers.\n".upper()
					continue

			
        print "Your {} result is {}.\n".format(operation,result).upper()  


    elif op_choice in ('sqr','squ','cub','sin','cos'):

        print "Thank you for choosing an operation.\n"              

        while True:

				num1 = raw_input('Please enter your number.\n')
	   
				try:
					
					if op_choice == 'sqr':
						
						result = squareRoot(num1)
						operation = "square root"
						break

					if op_choice == 'squ':
						
						result = square(num1)
						operation = "square"
						break
					
					if op_choice == 'cub':
						
						result = cube(num1)
						operation = "cube"
						break                        

					if op_choice == 'sin':
						
						result = sine(num1)
						operation = "sine"
						break                        

					if op_choice == 'cos':
						
						result = cosine(num1)
						operation = "cosine"
						break
					
				except:

					print "You need to enter numbers.\n".upper()
					continue

        print "Your {} result is {}.\n".format(operation,result).upper()  


    else:
        print "Invalid choice. Please try again.\n".upper()
        continue
    
    
    