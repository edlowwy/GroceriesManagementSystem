#Low Shao Xuan
#TP064058


def register(): #define fucntion 
    
    customerdata = [] #create an empty list  
    individual = [] #create an empty list 
    
    print("============Registration Form============") #print statement
    name = str(input("Please enter your name: ")) #read input from user as name

    while True: #while loop
        try: #test the code for error
            age = int(input("Please enter your age: ")) #read input from user as age
        except ValueError: #handle error while code is tested error
            print("Please enter a valid integer") #print statement
            continue #return to beginning of while loop
        else:
            break #break the loop
        

    while True: #while loop
        gender = input("What is your gender: ") #read input from user as gender
        if gender.lower() == "male" or gender.lower() == "female": #conditional statement 
            break #break the while loop
    
        else:
            print("Invalid entry") #print statement
            continue #return to beginning of while loop

    while True: #while loop
        try: #test the code for error
            dob = int(input("When is your birthday (DD/MM/YYYY): ")) #read input from user as dob
        except ValueError: #handle error while code is tested error
            print("Please enter a valid integer without '/'") #print statement
            continue #return to beginning of while loop
        else:
            break #break the while loop
        

    while True: #while loop
        try: #test the code for error
            contact = int(input("Please enter your contact number: ")) #read input from user as contact
        except ValueError: #handle error while code is tested error
            print("Please enter a valid integer") #print statement
            continue #return to beginning of while loop
        else:
            break #break the while loop

            
    userid = input("Please create a user ID: ") #read input from user as userid

    while True: #while loop
        password = input("Please create a password which contains 8 characters: ") #read input from user as password
        password2 = input("Please rewrite your password: ") #read input from user as password2
        if len(password)<8: #conditional statement 
            print("The entered password too short, please register again") #print statement
            continue #return to beginning of while loop

        elif(password2 != password): #conditional statement 
            print("Password doesn't match, please register again") #print statement
            continue #return to beginning of while loop
        else:
            break #break the while loop

    individual.append(name) #append the input from user into list 
    individual.append(str(age)) #append the input from user into list
    individual.append(gender) #append the input from user into list
    individual.append(str(dob)) #append the input from user into list
    individual.append(str(contact)) #append the input from user into list
    individual.append(userid) #append the input from user into list
    individual.append(password) #append the input from user into list
    
    customerdata.append(individual) #append another list into the list 

    cd = open("customer_data.txt",'a') #open text file as append

    for individual in customerdata: #for loop
        for record in individual: #for loop
            cd.write(record) #write item from list into text file
            cd.write('\t') #indicates blank space between each string  
        cd.write("\n") #indicates a new line 
        cd.close() #close the open text file 

    print("==========Your account has been successfully created==========") #print statement
    print("\n") #indicates a new line 
   


def viewdata(): #define fucntion
    ul = open('customer_data.txt','r') #open text file as read
    key = input("Please enter your name: ") #read input from user as key

    for line in ul: #for loop
        line = line.rstrip() #remove trailing whitespace 
        if not key.lower() in line.lower(): #conditional statement 
            continue #return to beginning of for loop
        print(line) #print statement
        
    ul.close() #close the open file  



def userlogin(): #define fucntion

    ul = open("customer_data.txt",'r') #open text file as read
    user = [] #create an empty list to store data 
    username = [] #create an empty list 
    password = [] #create an empty list 

    for line in ul: #for loop
        if not line.isspace(): #conditional statement
            line_strip = line.strip() #remove leading and trailing whitespace 
            line_split = line_strip.split() #split a string into a list 
            user.append(line_split) #append string into the list 
   
       
    for data in user: #for loop
        username.append(data[5]) #append the sixth item of another list into the list  

    for data in user: #for loop
        password.append(data[6]) #append the seventh item of another list into the list 


    while True: #while loop
        login1 = str(input("Please enter your username: ")) #read input from user as login1
        if login1 in username: #conditional statement 
            break #break the loop
        else:
            print("Invalid username") #print statement 
            print() #print an empty line 
            continue #return to beginning of while loop

    while True: #while loop
        login2 = str(input("Please enter your password: ")) #read input from user as login2
        if login2 == password[username.index(str(login1))]: #conditional statement
            break #break the loop
        else:
            print("Invalid password") #print statement 
            print() #print an empty line 
            continue #return to beginning of while loop

    print("============Registered Customer============\n") #print statement     
    while True: #while loop
        
        print("Would you like to:") #print statement
        print("1.View Personal Information\n2.View Grocery Details\n3.Purchase Grocery\n4.exit") #print statement
        ans = input("Please enter the number of your choice: ") #print statement
        
        if ans == '1': #conditional statement 
            viewdata() #call function
            continue #return to beginning of while loop

        elif ans =='2': #conditional statement 
            viewgrocery() #call function
            continue #return to beginning of while loop
        
        
        elif ans == '3': #conditional statement 
            buygrocery() #call function
            
            f = open("orderrecord.txt",'r') #open text file as read           
            line = f.readlines() #read each line of the text file as a list item
            line2 = ''.join(line) #combine the seperated item from list into a string 
                      
                         
            f2 = open("customerorder.txt",'a') #open text file as append
            f2.write(login1) #write input from user into text file 
            f2.write("\t") #indicates blank space between each string 
            f2.write(line2) #write item from list into text file
            f2.write("\n") #indicates a new line 

            f.close() #close the open test file
            f2.close() #close the open test file
            continue #return to beginning of while loop

       

        elif ans == '4': #conditional statement 
            break #break the while loop

        else:
            print("Invalid Entry") #print statement 
            continue #return to beginning of while loop





def adminlogin(): #define fucntion
    
    al = open("admin_data.txt",'r') #open text file as read
    admin = [] #create an empty list 
    username = [] #create an empty list 
    password = [] #create an empty list 

    for line in al: #for loop
        if not line.isspace(): #conditional statement 
            line_strip = line.strip() #remove leading and trailing whitespace
            line_split = line_strip.split() #split a string into a list
            admin.append(line_split) #append string into the list
        
       
    for data in admin: #for loop
        username.append(data[0]) #append the first item of another list into the list 

    for data in admin: #for loop
        password.append(data[1]) #append the second item of another list into the list 
        

    while True: #while loop
        login1 = str(input("Please enter your username: ")) #read input from user as login1
        if login1 in username: #conditional statement 
            break #break the loop
        else:
            print("Invalid username") #print statement
            print() #print an empty line 
            continue #return to beginning of while loop

    while True: #while loop
        login2 = str(input("Please enter your password: ")) #read input from user as login2
        if login2 == password[username.index(str(login1))]: #conditional statement 
            break #break the loop
        else:
            print("Invalid password") #print statement 
            print() #print an empty line 
            continue #return to beginning of while loop

    while True: #while loop

        print("============Admin Login============") #print statement
        print() #print an empty line 
        print("Would you like to:") #print statement
        print("1.Uplaod Groceries Detail\n2.View Grocery\n3.Update Grocery Detail\n4.Delete Groceries Information\n5.Search Groceries Detail\n6.View Orders of Customers\n7.Search Order of Cutomer\n8.Exit") #print statement

        option = input("Please enter the number of your choice: ") #read input from user as option

        if option == '1': #conditional statement 

            item_list = [] #create an empty list 
            gi_list = [] #create an empty list 
            
            name = input("Please enter the name of item: ") #read input from user as name
            price = input("Please enter the price of item: ") #read input from user as price         
            countryimport = input("Please enter the country of production: ") #read input from user as countryimport
            category = input("Please enter the category: ") #read input from user as category
            restockdate = input("Please enter the restock date: ") #read input from user as restockdate

            item_list.append(name) #append the input from user into list 
            item_list.append(price) #append the input from user into list 
            item_list.append(countryimport) #append the input from user into list 
            item_list.append(category) #append the input from user into list 
            item_list.append(restockdate) #append the input from user into list 

            gi_list.append(item_list) #append another list into the list

            gi = open("groceryinventory.txt",'a') #open text file as append

            for item_list in gi_list: #for loop
                for item in item_list: #for loop
                    gi.write(item) #write item from a list into the text file 
                    gi.write(' ') #indicates a blankspace between each line 
                gi.write("\n") #indicates a new line
                gi.close() #close the open text file 
                continue #return to beginning of while loop



        elif option == '2': #conditional statement 

            gi = open("groceryinventory.txt",'r') #open text file as read
            print("============Item available in the store============") #print statement
            print() #print an empty line 
            gi_list = gi.readlines() #read the text file as a list 

            for data in gi_list: #for loop
                print(data) #print statement
            gi.close() #close the open text file 
            continue #return to beginning of while loop
                        

        elif option == '3': #conditional statement 

            gi = open("groceryinventory.txt",'r+') #open text file as read and write 
            
            item = input("Please enter the grocery you would like to modify: ") #read input from user as item

            for line in gi: #for loop
                if not line.isspace(): #conditional statement 
                    line_strip = line.strip() #remove leading and trailing whitespace
                    line_split = list(line_strip.split()) #split the string into a list 
                    if item in line_split: #conditional statement 
                        print(line_split) #print statement 
                        change = input("1.name\n2.price\n3.category\n4.product's country\n5.restock date\nEnter the number of your choice that you would like to modify: ") #read input from user as change 
                        if change == "1": #conditional statement
                            name = input("Please enter the new name: ") #read input from user as name
                            line_split[0] = name #modify the first element of the list to the input 
                            x = line_split #define the new list with a new variable 
                            break #break the loop

                        elif change == "2": #conditional statement
                            price = input("Please enter the new price: ") #read input from user as price
                            line_split[1] = price #modify the second element of the list to the input 
                            x = line_split #define the new list with a new variable                              
                            break #break the loop
                        
                        elif change == "3": #conditional statement
                            category = input("Please enter the new category: ") #read input from user as category
                            line_split[2] = category #modify the third element of the list to the input 
                            x = line_split #define the new list with a new variable                              
                            break #break the loop

                        elif change == "4": #conditional statement
                            pc = input("Please enter the new product's country: ") #read input from user as pc
                            line_split[3] = pc #modify the fourth element of the list to the input 
                            x = line_split  #define the new list with a new variable                             
                            break #break the loop

                        elif change == "5": #conditional statement
                            rd = input("Please enter the new restock date: ") #read input from user as rd
                            line_split[4] = rd #modify the fifth element of the list to the input 
                            x = line_split #define the new list with a new variable                              
                            break #break the loop

                        else:
                            print("Invalid Entry") #print statement 
                            adminlogin() #call function 
                                                    
            gi.close() #close the open text file 
            file = open("groceryinventory.txt",'a+') #open text file as read and write 
            file.write("\n") #indicates a new line 
            file.write(str(x).replace("[","").replace("]","").replace(",","").replace("'","")) #write the modified string into text file 
            file.close() #close the open text file 

            f = open("groceryinventory.txt",'r') #open text file as read 
            lines = f.readlines() #read the text file as a list 
            f = open("groceryinventory.txt",'w') #open text file as write 
            for line in lines: #for loop
                if not line.startswith(item): #conditional statement 
                    f.write(line) #write string into text file 

            f.close() #close the open text file
            continue #return to beginning of while loop
              
            
        elif option == '4': #conditional statement 

            delete = input("Please enter the grocery you would like to delete: ") #read input from user as delete
            
            f = open("groceryinventory.txt",'r') #open text file as read 
            lines = f.readlines() #read the text file as a list 
            f = open("groceryinventory.txt",'w') #open text file as write
            for line in lines: #for loop               
                if not line.startswith(delete): #conditional statement 
                    f.write(line) #write string into text file

            f.close() #close the open text file
            continue #return to beginning of while loop
                
           



        elif option == '5': #conditional statement 

            gi = open('groceryinventory.txt','r') #open text file as read 
            key = input("Please enter the grocery name you would like to view: ") #read the input from user as key 

            for line in gi: #for loop
                line = line.rstrip() #remove trailing whitespace
                if not key.lower() in line.lower(): #conditional statement 
                    continue #return to the for loop
                print(line) #print statement 
                
            gi.close() #close the open text file 
            print("\n") #indicates a new line 
        


        elif option == '6': #conditional statement 

            f = open("customerorder.txt",'r') #open text file as read 
            f_read = f.readlines() #read the text file as a list 

            for data in f_read: #for loop
                print(data) #print statement 
            f.close() #close the open text file 
            print("\n") #indicates a new line 
            continue #return to beginning of while loop
        

        elif option == '7': #conditional statement 
        
            f = open('customerorder.txt','r') #open text file as read 
            key = input("Please enter the username of customer: ") #read input from user as key 

            for line in f: #for loop
                line = line.rstrip() #remove trailing whitespace
                if not key.lower() in line.lower(): #conditional statement 
                    continue #return to the for loop
                print(line) #print statement 
                    
            f.close() #close the open file 
            print("\n") #indicates a new line 
            continue #return to beginning of while loop




        elif option == '8': #conditional statement 
            print("\n") #indicates a new line
            break #break the loop
            



        else:
            print("Invalid Entry") #print statement
            continue #return to beginning of while loop
            
              

def viewgrocery(): #define fucntion

    gi = open("groceryinventory.txt",'r') #open text file as read 
    print("============Item available in the store============") #print statement
    print() #print an empty line 
    gi_list = gi.readlines() #read the text file as a list 

    for data in gi_list: #for loop
        print(data) #print statement 
    gi.close() #close the open text file 

       

            

def buygrocery(): #define fucntion

    gi_list = [] #create an empty list
    goods_name = [] #create an empty list
    goods_price = [] #create an empty list     
    shopping_cart = [] #create an empty list
    finalprice = [] #create an empty list

    gi = open("groceryinventory.txt",'r') #open text file as read 
    
    print("============Item available in the store============") #print statement
   
    for line in gi: #for loop
        if not line.isspace(): #conditional statement 
            line_strip = line.strip() #remove leading and trailing whitespace
            line_split = line_strip.split() #split the string into a list 
            gi_list.append(line_split) #append the string from text file into list 

        print(line) #print statement 
        
    for goods in gi_list: #for loop
        goods_name.append(goods[0]) #append the first item of another list into the list 

    for goods in gi_list: #for loop
        goods_price.append(goods[1]) #append the second item of another list into the list 

         
    print("="*55) #print statement 
    
    option = input("Enter yes to proceed to buy grocery: ")  #read input from user as option  
        
    while option.lower() == "yes": #while loop
        buyitem = input("Please enter the item you would like to purchase: ")  #read input from user as buyitem
        if buyitem in goods_name: #conditional statement 
            qtyitem = int(input("Please enter the purchase quantity of the item: ")) #read input from user as qtyitem          
            subtotal = int(goods_price[goods_name.index(buyitem)])*qtyitem #calculate the subtotal 
            print(subtotal) #print statement 
            shopping_cart.append(buyitem + ", " + "quantity: " + str(qtyitem) + "," + "subtotal: " + str(subtotal)) #append the input from user into list
            finalprice.append(subtotal) #append the subtotal into list 
            total = 0 #set the variable to "0"
            for i in range(0,len(finalprice)): #for loop
                total = total+finalprice[i] #calculate total 
            
            print(shopping_cart) #print statement
            option = input("Do you wish to add amy more groceries?\nEnter yes to proceed or no to exit: ") #read input from user as option  
            if option.lower() == "yes": #conditional statement 
                continue #return to beginning of while loop
            elif option.lower() =="no": #conditional statement 
            
                print("\n") #indicates a new line 
                print("============Final Bill============") #print statement
                print("\n") #indicates a new line 
                print(shopping_cart) #print statement 
                print("Your total payable amount is: ",total) #print statement
                print("\n") #indicates a new line 
                print("============Pay Section============") #print statement
                print("\n") #indicates a new line 
                    
                while True:
                    pay = float(input("Please enter the amount you would like to pay: ")) #read the input from user as pay 
                    if pay>=total : #conditional statement 
                        balance = pay - total #calculate balance
                        print("This is your balance: ",balance) #print statement 
                        print("\n") #indicates a new line         
                        break #break the loop
                    elif pay<total: #conditional statement 
                        print("Insufficient Balance") #print statement 
                        continue #return to beginning of while loop

                    else:
                        print("Invalid Entry") #print statement 
                        continue #return to beginning of while loop
                    
                        
                print("============Thank You============") #print statement
                print()

                f = open("orderrecord.txt",'a') #open the text file as append 
                for i in shopping_cart: #for loop
                    f.write(i) #write string from another list into the text file
                f.write("\n") #indicates a new line           
                f.close() #close the open text file 
                
        else:
            print("Invalid entry, item not found") #print statement

  
def mainmenu(): #define fucntion
        
        print("============Welcome to FRESHCO Sdn Bhd============") #print statement
        print("Hi there! Who are you logging in as: ") #print statement
        print("1.New customer\n2.Registered Customer\n3.Admin\n4.Exit") #print statement
        option = input("Please enter the number of your choice: ") #read the input from user as option 
        if option == '1': #conditional statement 
            print("\n") #indicates a new line
            print("============New Customer============") #print statement
            print("Would you like to: ") #print statement
            print("1.Register an account\n2.Continue as guest to view groceries details") #print statement
            ans = input("Please enter the number of your choice: ") #read the input from user as ans
            print("\n") #indicates a new line
            
            if ans == '1': #conditional statement 
                register() #call function 
                while True: #while loop
                    out = input("Please enter q to exit to mainmenu: ") #read the input from user as out 
                    if out.lower() == "q": #conditional statement 
                        print("\n") #indicates a new line 
                        mainmenu() #call function 
                        
                        
                    else:
                        print("Invalid Entry")
                        continue #return to beginning of while loop
                

            elif ans == '2': #conditional statement               
                viewgrocery() #call function 

                while True: #while loop
                    out = input("Please enter q to exit to mainmenu: ")
                    if out.lower() == "q": #conditional statement 
                        print("\n") #indicates a new line 
                        mainmenu() #call function 
                    
                        
                    else:
                        print("Invalid Entry") #print statement
                        continue #return to beginning of while loop
                        
            else:
                print("Invalid Entry") #print statement

        elif option == '2': #conditional statement 
                userlogin() #call function 
                mainmenu() #call function 
                
                           
        elif option == '3': #conditional statement 
                adminlogin() #call function 
                mainmenu() #call function 

        elif option == '4': #conditional statement 
            print("\n\n") #indicates a new line 
            print("=============Hope to see you again=============") #print statement
            print("=================System Closed=================") #print statement
            
            

        else:
            print("Invalid Entry") #print statement
            mainmenu() #call function 


            

#mainprogram
mainmenu() #call function