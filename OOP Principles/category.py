'''
# Creating a module with a class for storing and mutating value involving budgeting
'''
class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget
    
    # Getter and Setter Methods for the budget of Entertainment, Utilities, and Food
    def set_name(self, name):
        self.__name = name
        
    def set_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
  
    def get_name(self):
        return self.__name

    def get_budget(self):
        return self.__allocated_budget

    
    # Budget functionalities
    def add_expenses(self, amount):
        if self.__allocated_budget > amount:
            self.__remaining_budget -= amount
        else:
            print("You exceeded your budget...")   

    def display_category_summary(self):
        print(f"Budget for {self.__name}: Initial Budget: {self.__allocated_budget} Remaining Budget: {self.__remaining_budget}")

