from random import randint
from random import seed 
import random 
import string 

department = input ("enter your department ")
department = department.lower ()
random_number = 0

if department =='FinOps' or department == 'Marketing ' or department == 'Accounting':
     instances_number = int(input("Enter the number of EC2 instances you need:"))
     count = 1 
     
     def get_random_string(length):
         result_str = ''.join(random.choice(string.ascii_letters) for i in range(5))
         return result_str
         
         while instance_number >= count:
             random_number = randint(10000, 99999)
             print ("EC2-"+department+'-'+get_random_string(5)+str(random_number))
             count += 1 
else:
        print("who gave you permission? Punk! to use this Name Generator as the only Departments currently supported are: Finops, Acounting, and Marketing. ")