class Category:
    def __str__(self):#this will display all the transaction that has taken place in the budget.
       print(str(int((30-len(self.name))/2)*"*")+self.name+str(int((30-len(self.name))/2)*"*"))
       for i in self.ledger:
           shorten_description = i["description"][:23]#cutting the string into 23 characters
           print('{:23s}{:7.2f}'.format(shorten_description, i["amount"]))
       Total = "Total: " + str(self.get_balance())
       return Total
       
    def __init__(self,name):
        self.name = name
        self.ledger = []#taking all our entry

    def deposit(self,amount,description=""):
        new_deposit = {"amount":amount, "description":description}
        self.ledger.append(new_deposit)


    def withdraw(self,amount,description=""):
        withdraw = {"amount":-abs(amount),"description":description}
        #check if there are available fund
        if(self.check_funds(amount)): 
            self.ledger.append(withdraw)
            return True
        else: return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance = balance + i["amount"]
        return balance
    
    def transfer(self, amount, destination):
        #check if the amount can be successfully withdrawn before 
        if(self.withdraw(amount, "Transfer to " + str(destination.name)) == True):
            #if the withdrawal was successful
            destination.deposit(amount,"Transfer from " + self.name)
            return True
        return False
   
    def check_funds(self, amount):
        funds_available = False if(amount > self.get_balance()) else True
        return funds_available

 #################### The below code is not part of the module need to be created##################################
    def total_amount_deposited(self):
        total_amount_deposited = 0
        for ledger in self.ledger: 
           if ledger["amount"] >= 0:
               total_amount_deposited = total_amount_deposited + ledger["amount"]
        return total_amount_deposited


    def total_amount_withrawn(self):
        total_amount_withrawn = 0
        for ledger in self.ledger:
           if ledger["amount"] < 0: 
               total_amount_withrawn = total_amount_withrawn + abs(ledger["amount"])
        return total_amount_withrawn
              


def create_spend_chart(categories): 
   categories_spent = []#contain the name of the category and the percentage spent.
   for category in categories:
       category_in_percentage = ((category.total_amount_withrawn())/(category.total_amount_deposited()))*100
       category_in_percentage = int(round(category_in_percentage,-1))#converting it to the nearest ten
       category_spent = {category.name: category_in_percentage}
       categories_spent.append(category_spent)
   

   percentage_bars = [] #this will hold the percentage with the number of bars to be displayed
   for i in range(100,-10,-10):
      bars = []
      for j in categories_spent:
          categories_value = list(j.values())[0] #passing the percentage values in the  categories_value variable
          bars += "o" if(i <= categories_value) else " " #getting the "o" to be displayed on the bar chart
      percentage_bars.append({i:bars})
   return display_chart(percentage_bars, categories)
   
def display_chart(x,y):
    print("\nPercentage spent by category")
    for i in x:
        display_bars = "  ".join(list(i.values())[0])#displaying the bar with two spacing from the previous bar
        display_percentage = str(list(i.keys())[0])
        print('{:>3s}|'.format(display_percentage), display_bars)
    print(" "*4+"-"*(len(display_bars) + 1)+"-"*2)#the horinzontal dashes below the bar chart
    
    #getting the category that has the highest name length
    names_of_category = []
    max_len_of_category_name = ""
    for j in y:
        names_of_category.append(j.name)
        if(len(max_len_of_category_name) < len(j.name)):
            max_len_of_category_name = j.name.lower()
    max_len_of_category_name = len(max_len_of_category_name)#converting back to the length of the string
    
    #extracting and displaying the names in vertical order
    for column in range(0,max_len_of_category_name + 1):
        vertical_display = ""
        for row in range(0, len(names_of_category)):
            try:
                vertical_display += (names_of_category[row][column] + " "*2)#adding two spacing to the names of the category
            except:
                vertical_display += (" " + " "*2) #adding two spacing to the names of the category
        print(" "*5 + vertical_display)#displaying the names vertically under the bar chart