class Ingredient:
    def __init__(self,name,amount,unit):
        self.name=name
        self.amount=amount
        self.unit=unit
    def __str__(self):
        return f"{self.amount}{self.unit} of {self.name}"
    
    def __add__(self, other):
        if isinstance(other,Ingredient):
            if self.name==other.name and self.unit ==other.unit:
                total=self.amount+other.amount
                return Ingredient(self.name,self.amount,self.unit)
            return NotImplemented
        
class Recipe:
    def __init__(self,name):
        self.name=name
        self.ingredients=[]

    def add_ingredient(self,ingredient):
        for i,item in enumerate(self,self.ingredients):
            if item.name == ingredient.name and item.unit == ingredient.unit:
                self.ingredients[i] = item + ingredient
            else:
                self.ingredients.append(ingredient)

flour1 = Ingredient("Flour", 200, "g")
flour2 = Ingredient("Flour", 100, "g")
sugar = Ingredient("Sugar", 50, "g")
water = Ingredient("Water", 1, "cup")

print(flour1 + flour2)

    
        


    
        