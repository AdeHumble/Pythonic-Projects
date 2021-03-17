#Python Standard Libraries Adopted
import shutil as sh
import random
import string
import datetime


#Homepage Design $ Instructions for use[line 11-26]

#Line11 will gets the console width/size. It is necessary so as that the center method can properly aligned text to the center of any type of IDE 
console_size=sh.get_terminal_size().columns
print(("***"*15).center(console_size))
print("Welcome to ADEHUMBLE SUPERMARKET".center(console_size))
print("Home of Groceries".center(console_size))
print(("***"*15).center(console_size))
print()
#Line18 to Line26 represents the available actions this software can perform
print("A: ||Press 'A' to add new items to the Supermarket stock||")
print("D: ||Press 'D' to remove an item from the list of current stock")
print("L: ||Press 'L' to list all the available stocks||")
print("I: ||Press 'I' to inquire about a particular item||")
print("R: ||Press 'R' to remove purchased items from a customer's cart before checking out||")
print("P: ||Press 'P' to purchase new items from the Supermarket stock||")
print("C: ||Press 'C' to checkout purchased items and make payment||")
print("Q: ||Press 'Q' to quit a transaction||")
print("H: ||Press 'H' to view all available possible actions again||")


#Parameters Initialisation[line 30-38]
item_unit_price={}
item_description={}
item_unit_stock={}
cart_details_price={}
cart_details_qty={}
cart_items_unit={}
action="y"
total=[]
total_cost=0


#Function that will generates receipts for every completeded transactions/purchase[line 43-80]

def Receipt():
		
	#Generates a unique Transcation ID for every completed transactions[line 46-54]
	transact_ID=[]
	rand_chr=list(str(random.random()*5))
	if '.' in rand_chr:
		rand_chr.remove('.')	
	rand_num_list=list("".join(rand_chr))
	alpha_list=list(string.ascii_uppercase)
	transact_ID.extend(alpha_list)
	transact_ID.extend(rand_num_list)
	transaction_ID="".join(random.sample(transact_ID,10))
	
	#Generates the date and time specifics for each successful transaction[line57]
	purchase_time=datetime.datetime.today()
	
	#Format the receipt output in a unique way[line 60-81]
	print()
	print(("***"*15).center(console_size))
	print("ADEHUMBLE SUPERMARKET".center(console_size))
	print("Home of Groceries".center(console_size))
	print()
	print("BILL PAYMENT".center(console_size))
	print()
	print("Reference Number: ", transaction_ID)
	print("Date of Transaction: ",purchase_time.strftime("%A;%B %d, %Y"))
	print("Time of Transaction: ",purchase_time.strftime("%I:%M:%S %p"))
	print()
	print("Below are the list of items purchased with their respective costs\n")
	
	#Iterates over two different dictionaries instantaneously[line 74&75]
	for (k1,v1), (k2,v2) in zip(cart_details_price.items(),cart_items_unit.items()):
		print("{}units of {} costs ₦{}".format(v2,k1,v1))
		
	print()
	print(f"TOTAL COST = ₦{total_cost}".center(console_size))
	print()
	print("\nThank you for patronizing us. We woud like to see you again Have a nice day!")
	print(("***"*15).center(console_size))


#Opens up and extracts the text file containing the product information and stores this information in their respective dictionaries as declared above[line 86-112]

with open("project.txt","r") as product_details:
	
	#The first line of the text file represents the number of items presently available[line89]
	no_items=int((product_details.readline()).rstrip("\n"))
	
	#Extracts data into the item_unit_price dictionary[line 92-97]
	for i in range(no_items):
	    file_line=(product_details.readline()).rstrip("\n")
	    a,b=file_line.split(":")
	    a=int(a)
	    b=float(b)
	    item_unit_price.update({a:b})
	
	#Extracts data into the item_description dictionary[line 100-104]
	for i in range(no_items):
	    file_line=(product_details.readline()).rstrip("\n")
	    a,b=file_line.split(":")
	    a=int(a)
	    item_description.update({a:b})
	
	#Extracts data into the item_unit_stock dictionary[line 107-112]
	for i in range(no_items):
	    file_line=(product_details.readline()).rstrip("\n")
	    a,b=file_line.split(":")
	    a=int(a)
	    b=int(b)
	    item_unit_stock.update({a:b})


#The engine room. The while loop contains codes for all the available/possible actions[line 118-510]

#Quit Action Logistics[line 118-176]
while (action!="q" or action!="Q"):
    action=input("What would you like to do? ")
    
    #When a user quits the software without performing any transaction or using any of the service. Nothing should change about the current state of the shop[line 122-124]
    if ((action=="" or action=="q" or action=="Q") and (total_cost==0)):
    	print()
    	print("Good!\n I trust you had a sweet experience using this software.\nStay Safe...Bye!")
    	break
    
    #When a user quits the software without checking out AFTER a purchase[line 128-176]	
    elif ((action=="q" or action=="Q" or action=="") and (total_cost>0)):
    	
    	check=input("Some items have already been purchased into the cart.Do you really want to quit now?\n\n1)Press 'y' for YES If you want to quit now and generate a receipt for this transaction\n2)Press 'n' for NO if you wish to continue\n3)Press 't' to forcefully terminate this transaction\n ")
    	
    	#if they really want to quit and make purchase[line 133-160]	
    	if (check=="y" or check=="Y"):
    		for i in cart_items_unit:
    			item_unit_stock[i]-=cart_items_unit[i]
    		print("Take your transaction receipt")
    		Receipt()
    		
	    	#Reset the customer's cart in case of another different transaction[line 140-143]
	    	cart_details_qty={}
	    	cart_details_price={}
	    	cart_items_unit={}
	    	total_cost=0
	    	
	    	#Update the stock because some items have been purchased. Hence, the quantity/stock of the purchased items should change[line 146-157]
	    	with open("project.txt", "w") as product_details:
	        	no_items=len(item_unit_price)
	        	product_details.write(str(no_items)+"\n")
	        	
	        	for j in item_unit_price:
	        		product_details.write(str(j)+":"+str(item_unit_price[j])+"\n")
	        	
	        	for j in item_description:
	        		product_details.write(str(j)+":"+str(item_description[j])+"\n")
	        	
	        	for j in item_unit_stock:
	        		product_details.write(str(j)+":"+str(item_unit_stock[j])+"\n")
	    	
	    	print("I trust you had a sweet experience using this software.\nStay Safe...Bye!")
	    	break
    	
    	#if a user denounce his/her action as a mistake and would like to continue using the software
    	elif (check=="n" or check=="N"):
    		print("Okay, Good!. I guessed as much\nPlease, press 'P' to continue to make purchase or press 'C' to check out")
    		continue
    	
    	#if a user wishes to quit without buying for the items in his/her cart.
    	if (check=="t" or check=="T"):
    		print()
    		print("Good! You won't be charged. Your transaction history has been deleted.\n I trust you had a sweet experience using this software.\nStay Safe...Bye!")
    		break
    	
    	#if an unexpected input was entered
    	else:
    		print("That's a wrong input!")
    		print("You may press 'Q' to quit")
    
    
    #The purchase action logistic[line 180-252]  
    elif (action=="p" or action=="P"):
        
        try:
        	item_no=abs(int(float(input("Enter the item number you wish to purchase: "))))
        	
        except ValueError:
        	print()
        	print("That was a wrong input! You need to enter a number. Please, try all over again")
        	continue
        print()
        
        #if the item to be purchased is available[line 192-252]
        if (item_no in item_description):
        	item_name=item_description[item_no]
        	print(f"Okay! You wish to purchase {item_name}")
        	try:
        		item_unit=int(float(input(f"How many units of {item_name} do you wish to buy? ")))
        	
        	except ValueError:
        		print()
        		print("That was a wrong input! You need to enter a number. Please, try all over again")
        		continue
        	print()
        	
        	if (item_unit<=0):
        		print("Item unit must be greater than zero")
        		print()
        		continue
        	#If there is enough stock to cater for tge units a customer what to buy AND the item is not present in customer cart as of the moment[line 109-246]	
        	elif ((item_unit_stock[item_no]>=item_unit) and (item_no not in cart_items_unit)):
        		
        		a1=item_name 		
        		b1=item_unit_price[item_no]*item_unit
        		c1=item_unit
        		d1=item_no
        		
        		cart_details_price.update({a1:b1})
        		cart_details_qty.update({a1:c1})
        		cart_items_unit.update({d1:c1})
        		total=cart_details_price[item_name]
        		total_cost+=total
        		
        		print(f"{item_unit} units of {item_name} has been added to cart at the cost of ₦{b1}")
        		print(f"Below is a view of your cart information\n{cart_details_qty}")
        		print()
        		print("Press 'P' to purchase more. Would you like to check out? Press 'C' or Press 'Q' to quit")
        		print()
        	
        	#If the item is already among the list of items in the cart, ready to be bought[line 129-240]
        	elif ((item_no in cart_items_unit) and (item_unit+cart_items_unit[item_no]<=(item_unit_stock[item_no]))):		
        		new_price=item_unit_price[item_no]*item_unit
        		cart_items_unit[item_no]+=item_unit
        		cart_details_qty[item_name]+=item_unit
        		cart_details_price[item_name]+=new_price
        		total_cost+=new_price
        		
        		print(f"{item_unit} of {item_name} has been added again to cart at the cost of ₦{new_price}")
        		print(f"Below is a view of your cart information\n{cart_details_qty}")
        		print()
        		
        		print("Press 'P' to purchase more. Would you like to check out? Press 'C' or Press 'Q' to quit")
        		
        	else:
        		print(f"There are not enough stocks presently for this order. Kindly persuade the customer to reduce his/her order quantity or contact the manager to add more stocks of {item_name}")
        		print()
        		
        		print("Press 'C' if you would like to check out now or Press 'Q' to quit")
        		print()
        				
        else:
        	print("Sorry! We currently do not have the item you are requesting to buy")
        	print()
        	print("Press 'P' to purchase other items or Press 'Q' to quit")
    
    
    #The remove action logistics[line 256-326]
    elif (action=="r" or action=="R"):
    	
    	#It is not going to do anything beacause the customer has not added any item to his/her cart. So there is nothing to remove[line 259_263]
    	if (total_cost==0):
    		print("Your cart is currently empty. You have not make any purchase")
    		print("Press 'P' to make a purchase or press 'Q' to quit")
    		print()
    		continue
    	else:
    		try:
    			item_no_2remove=abs(int(float(input("Enter the item number you wish to remove from the cart: "))))
    		except ValueError:
    			print()
    			print("That was a wrong input! You need to enter a number. Please, try all over again")
    			continue
    		
    	#If the item to remove is among what the customer has added to his/her cart. This block will confirm if the cutstomer really wishes to remove that item and also check whether the number of units a customer wishes to remove from his/her cart is less than or upto what he/she has initially purchased[line 273-326]
    	if (item_no_2remove in cart_items_unit):
    		item_name=item_description[item_no_2remove]
    		
    		check=input(f"Are you sure you want to remove {item_name}?.\nPlease, enter 'y' for YES or 'n' for NO: ")
    		
    		if (check=="y" or check=="Y"):
    			print()
    			remove_unit=int(input("How many unit(s) would you like to remove from the cart? "))
    			if remove_unit<cart_items_unit[item_no_2remove]:
    				unitprice_2remove=item_unit_price[item_no_2remove]
    				totalprice_2remove=unitprice_2remove*remove_unit
    				cart_details_qty[item_name]-=remove_unit
    				cart_details_price[item_name]-=totalprice_2remove
    				cart_items_unit[item_no_2remove]-=remove_unit
    				total_cost-=totalprice_2remove
    				print(f"{item_name} has been successfuly removed from your cart and necessary changes to your total cost")
    				print(f"Below is a view of your cart information\n{cart_details_qty}")
    			
    				
    			elif (remove_unit==cart_items_unit[item_no_2remove]):
    				print()
    				unitprice_2remove=item_unit_price[item_no_2remove]
    				totalprice_2remove=unitprice_2remove*remove_unit
    				
    				total_cost-=totalprice_2remove
    				
    				del (cart_items_unit[item_no_2remove])
    				del (cart_details_qty[item_name])
    				del (cart_details_price[item_name])
    				
    				print(f"{item_name} has been successfuly removed from your cart and necessary changes to your total cost")
    				print(f"Below is a view of your cart information\n{cart_details_qty}")
    		
    			else:
    				print("Sorry! You have a lesser purchase")
    				print("You can continue by pressing 'P' to make more purchase or press 'C' to check out now")
    					
    		elif (check=="n" or check=="N"):
    			print()
    			print("Ok Good!")
    			print("Press 'P' to purchase more. Would you like to check out? Press 'C' or Press 'Q' to quit")
    			print()
    			continue
    			
    		else:
    			print()
    			print("That's incorrect! Anyway, i'll take that as a NO")
    			print("You can continue by pressing 'P' to make more purchase or press 'C' to check out")
    			print()
    			
    	else:
    		print(f"Oops! You have not purchased any item named {item_name}.")
    		print("Would you like to check out now? Press 'C'. You can press 'Q' to quit")
    		print()
    	#Updates changes to the text file		
    	with open("project.txt", "w") as product_details:
    		no_items=len(item_unit_price)
    		product_details.write(str(no_items)+"\n")
    		
    		for j in range(no_items):
    			product_details.write(str(j+1)+":"+str(item_unit_price[j+1])+"\n")
    		
    		for j in range(no_items):
    			product_details.write(str(j+1)+":"+str(item_description[j+1])+"\n")
    		
    		for j in range(no_items):
    			product_details.write(str(j+1)+":"+str(item_unit_stock[j+1])+"\n")
    			
    		
    #The check out action logistic[line 343-381]		
    elif (action=="C" or action=="c"):
    	print()
    	
    	#To check out means to pay for the cart items at the counter of a customer representative. Obviously, there a customer cannot check-out/pay for items, if he /she has not added anything to his/her cart. Hence, total cost must me more than zero before a customer can check out
    	if (total_cost>0):
    		for i in cart_items_unit:
    			item_unit_stock[i]-=cart_items_unit[i]
    			
    		#This will call the receipt function from [line 43-80]
    		Receipt()
    		
    		print()
    		print("Mind you, you can still purchase items after check out, your cart has been reset. To quit press 'Q'")
    		print()
    		
    		#This will set the virtual cart to zero. This is necessary so that another customer wont have to pay for the goods of a previous customer
    		cart_details_qty={}
    		cart_details_price={}
    		cart_items_unit={}
    		total_cost=0
    		
    	else:
    		print("You have not make any purchase. Your cart is currently empty")
    		print("Press 'P' to make a purchase or press 'Q' to quit")
    		print()
    	
    	#updates the current changes to the stock i.e. into the text file
    	with open("project.txt", "w") as product_details:
        	no_items=len(item_unit_price)
        	product_details.write(str(no_items)+"\n")
        	
        	for j in item_unit_price:
        		product_details.write(str(j)+":"+str(item_unit_price[j])+"\n")
        	
        	for j in item_description:
        		product_details.write(str(j)+":"+str(item_description[j])+"\n")
        	
        	for j in item_unit_stock:
        		product_details.write(str(j)+":"+str(item_unit_stock[j])+"\n")
    
    
    #The add action logistic[line 385-430]
    elif (action=="a" or action=="A"):
        try:
        	#Ask for all the details about the item you wish to add
        	item_no=abs(int(float(input("Enter the item number you wish to add to stock: "))))
        	item_price=float(input("Enter the unit price for new item: "))
        	item_stock=abs(int(float(input("How many units of this new item do you wish to add to the stock? "))))
        	item_desc=input("Enter the name of this new item: ")
        		
        except ValueError:
        	print()
        	print("That was a wrong input! You need to enter a number. Please, try all over again")
        	continue
        
        #One good thing is that if the item number entered already exist, these lines of code will keep iterating, checking the next number until it got a unique number to itself[line 399-403]
        while (item_no in item_unit_stock):
        	item_no+=1
        	
        print()	
        print(f"That item number already exist. Changing value to {item_no}")
        
        if (item_desc in item_description.values()):
        	print(f"Oopsss! An item with a name of {item_desc} already exists. Try again by changing the name.")
        	print()
        	continue
        	
        else:
	        #Updates the new item information
	        item_unit_stock.update({item_no:item_stock})
	        item_description.update({item_no:item_desc})
	        item_unit_price.update({item_no:item_price})
         
        #writes the current changes to the text file[line 417-427]
        with open("project.txt", "w") as product_details:
        	no_items=len(item_unit_price)
        	product_details.write(str(no_items)+"\n")
        	
        	for j in item_unit_price:
        		product_details.write(str(j)+":"+str(item_unit_price[j])+"\n")
        	
        	for j in item_description:
        		product_details.write(str(j)+":"+str(item_description[j])+"\n")
        	
        	for j in item_unit_stock:
        		product_details.write(str(j)+":"+str(item_unit_stock[j])+"\n")
        
        print(f"Completed! {item_desc} has successfully been added to the supermarket stock")
      
          
    #The delete action logistic[line 433-477]
    elif (action=="D" or action=="d"):
    	try:
    		itemno_2del=abs(int(float(input("Enter the item number you wish to delete from the stock: "))))
    	except ValueError:
    		print()
    		print("That is a wrong input! Try again")
    		continue
    	
    	#Will confirm if the item you wish to delete is even among the supermarket stock/goods in the first place. If true, it'll delete all the information about that item[line 443-462]	
    	if (itemno_2del in item_unit_stock):
    		item_name=item_description[itemno_2del]
    		check=input(f" Are you sure you want to delete {item_name}?\nIf YES, press 'y'. But if NO, press 'n':  ")
    		if (check=='y' or check=='Y'):
    			
    			#updates the new information
    			del (item_unit_stock[itemno_2del])
    			del (item_description[itemno_2del])
    			del (item_unit_price[itemno_2del])
    			
    		elif (check=="N" or check=="n"):
    			print()
    			print("Okay! That must be a mistake then. You may quit by pressing 'Q'")
    			
    		else:
    			print()
    			print("That was a wrong.input. Bye!")
    	else:
    		print()
    		print("That item number does not exist in the first place. Thank you!")
    			
    	#writes the current changes to the text file[line 464-472]		
    	with open("project.txt", "w") as product_details:
    		no_items=len(item_unit_price)
    		product_details.write(str(no_items)+"\n")
    		for j in item_unit_price:
    			product_details.write(str(j)+":"+str(item_unit_price[j])+"\n")
    		for j in item_description:
    			product_details.write(str(j)+":"+str(item_description[j])+"\n")
    		for j in item_unit_stock:
    			product_details.write(str(j)+":"+str(item_unit_stock[j])+"\n")
    		
    		print()
    		print(f"{item_name} has successfully been deleted from the stock")
    		print("Would you like to continue using this software? Press any available keys. Otherwise, press 'Q' to quit")
    		print()
    				
    		
    #The list action logistic[line 482-489]
    elif (action=="L" or action=="l"):
    	print("Below is a list of all the current stocks")
    	print()
    	
    	#Iterates over three different dictionaries instantaneously[line 487 & 488]
    	for (k1,v1), (k2,v2), (k3,v3) in zip(item_description.items(),item_unit_price.items(), item_unit_stock.items()):
    		print("{} represents {}. It remains {}units".format(k1,v1,v3))
    	print()
    
    
    #The inquire action logistic[line 493-512]
    elif (action=="I" or action=="i"):
    	try:
    		itemno_2find=abs(int(float(input("Enter the item number you wish to inquire about: "))))
    	except ValueError:
    		print()
    		print("That is a wrong input! Try again")
    		continue
    	
    	#Checks if the product you want to enquire about is among the supermarket list of items. If true, it will search for and return all its details[line 502-510]		
    	if (itemno_2find in item_unit_stock):
    		print()
    		item_name=item_description[itemno_2find]
    		
    		#Format the result of your enquiry
    		print("{} represents {}\nThere are {} units of {} remaining in stock\n1 unit of {} costs ₦{}".format(itemno_2find, item_description[itemno_2find], item_unit_stock[itemno_2find], item_description[itemno_2find], item_description[itemno_2find], item_unit_price[itemno_2find]))
    		print()
    		print("You may quit by pressing 'Q'")
    		print()
    	else:
    		print("That item is not available in stock")
    		print()
    		
    	
    #The help action logistic[line 517-532]
    elif (action=="H" or action=="h"):
    	print()
    	
    	#At every point of pressing "H" or "h", the program will prints out the list of all available actions
    	print("INSTRUCTIONS FOR USE".center(console_size))
    	print("A: ||Press 'A' to add new items to the Supermarket stock||")
    	print("D: ||Press 'D' to remove an item from the list of current stock")
    	print("R: ||Press 'R' to remove purchased items from a customer's cart before checking out||")
    	print("L: ||Press 'L' to list all the available stocks||")
    	print("I: ||Press 'I' to inquire about a particular item||")
    	print("P: ||Press 'P' to purchase new items from the Supermarket stock||")
    	print("C: ||Press 'C' to checkout purchased items and make payment||")
    	print("Q: ||Press 'Q' to quit a transaction||")
    	print("H: ||Press 'H' to view all available possible actions again||")
   
    	print("If you have further questions or concerns, please contact the Manager. You can may press 'Q' to quit")
    	print()
    
    else:
    	print()
    	print("That's a wrong input. Kindly contact the admin for help in case you can't use this software.\nYou can also press 'H' for help on the list of possible inputs.\nThanks!")
    	print()