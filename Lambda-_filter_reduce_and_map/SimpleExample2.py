"""
Write a Python program, which returns a list with 2-tuples.
Each tuple consists of a  order number and the product of the price per items and the quantity. 
The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
"""
#           Order No      Book name              Quantity Price    
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

min_order = 100

invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),  #2nd
			              map(lambda x: (x[0],x[2] * x[3]), orders)))  #1st  

"""
1st:map(lambda x: (x[0],x[2] * x[3]), orders)
This returns a sequence 
[('34587', 163.8),
 ('98762', 284.0),
 ('77226', 98.8500),
 ('88112', 74.97)]
This is nothing but the sequence for the 2nd map function
"""
"""
2nd:map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10 , # **the new sequence above** 
This returns X as it is OR adds 10 to the price if less than 100 and keeps order no. same
"""
print(invoice_totals)
"""
                                                                   #<100 =>74.97+10(from above)                   
[('34587', 163.8), ('98762', 284.0), ('77226', 108.8500), ('88112', 84.97)]
"""
