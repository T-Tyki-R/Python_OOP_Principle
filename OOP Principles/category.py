'''
# 
'''
class BudgetCategories:
    def __init__(self, entertainment, utilities, food):
        self.__entertainment = entertainment
        self.___utilities = utilities
        self.__food = food
    
    # Getter and Setter Methods for the budget of Entertainment, Utilities, and Food
    def set_entertainment(self, e_bill):
        self.__entertainment = e_bill
        
    def set_entertainment_budget(self):
        self.__entertainment = 100

    def set_utilities(self, u_bill):
        self.___utilities = u_bill

    def set_utilities_budget(self):
        self.___utilities = 200

    def set_food(self, f_bill):
        self.__food = f_bill

    def set_food_budget(self):
        self.__food = 200

    def get_entertainment_budget(self):
        return self.__entertainment

    def get_utilities_budget(self):
        return self.___utilities

    def get_food_budget(self):
        return self.__food
    
    # Budget functionalities
    def add_expenses(self, amount):
        print("1. Entertainment\n2. Utilities\n3. Food\n")
        user_choice = int(input("Which category do you pick? "))
        amount = float(input("How much this you spend on this expense?: "))
        if user_choice == 1:
            if self.get_entertainment_budget() > amount:
                self.set_entertainment_budget(self.get_entertainment_budget()) - amount
            else:
                print("You exceeded your budget...")
        elif user_choice == 2:
            if self.get_utilities_budget() > amount:
                self.set_entertainment_budget(self.get_utilities_budget() - amount)
            else:
                print("You exceeded your budget...")
        elif user_choice == 3:
            if self.get_food_budget() > amount:
                self.set_food_budget(self.set_food_budget - amount) 
            else:
                print("You exceeded your budget...")
        else:
            print("You picked an invalid option")


    def display_category_summary(self):
        pass


food_category = BudgetCategories("food", 500)
food_category.add_expenses(100)
# food_category.display_category_summary()   
    


  
