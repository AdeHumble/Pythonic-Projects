Title: ScholarNetworkPythonProject
Project_Title: SMEs Inventory Management Software
Author: AdeHumble
First_Edition: April 29th, 2020
File name: "project.py". There are other unrelated python project files as well

This program is designed as a back-end software for any SME's (e.g. supermarket) to be used by a customer representative


A lot of Mathematical reasoning was factored into this program. All possible unfavorable real-life scenarios that could arise was considered and duly managed to the best of my knowledge


With the aid of this software, the representative can manage sales inventories and item stocks
	Can determine if a particular product is available
	Can edit some information about a particular product(e.g. product name, price and quantity)
	Can add a new product to the stock
	Can remove a particular product from the stock


It also allows a customer representative to check out the list of all items purchased by a customer, make payment and generate a receipt with a UNIQUE transacation ID FOR EACH purchase made at the counter
	In case a customer decides not to make purchase again after adding list of items to his/her cart, the customer representative can simply quit the software without checking out
	In case the customer representative MISTAKENLY ATTEMOTED TO QUIT THE SOFTWARE WITHIUT CHECKING OUT a customer's purchase, the software will raise an alert to confirm his/her decision


This software is also designed to save changes upon every SUCCESSFUL AND COMPLETED transactions into a file
	The file will only get updated if a customer make payment for his/her purchase
	If not, all the transcation history will simply be cleared out of memory


You may still find out other functionalities while you use this software. In case you encountered any difficulty in using this software or you have ideas on how this program can become more efficient, feel free to reach me via +2348122230304. Thanks!


#Pls, don't worry abiut this. 
for (k1,v1), (k2,v2), (k3,v3) in zip(item_unit_stock.items(), item_description.items(), item_unit_price.items()):
    			print(f"Below is all the current information about {itemno_2find}")
    			print()
    			print("{} represents {}\nThere are {} units of {} remaining in stock\n{} unit of {} costs {}".format(k1,v2,v1,v2,k1,v2,v3))