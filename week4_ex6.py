class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if self._price < 0:
            raise ValueError("Price cannot be negative")
        self._price=value 

    def __str__(self):
        return f"{self.name}: ${self._price:.2f}"
    
    def __eq__(self,other):
        if isinstance(other, Item):
                return other.name == self.name
        
    def cost(self):
         return self._price
    

    def __str__(self):
        return f"{super().__str__()} -> {self.cost()} (-{100 * self.discount}%)"


class Cart:
    def __init__(self, items=None):
        self.items = items if items is not None else []
        
    def add(self, item):
        self.items.append(item)
        
    def __len__(self):
        return len(self.items)
    
    def __add__(self, other):
        # Assuming 'other' is another Cart object
        merged_list = self.items+other.items
        return Cart(merged_list)
    
    def total(self):
        total=sum(item.cost() for item in self.items)
        return total 
    
    def summary(self):
        for item in self.items:
            print(item)
        print(self.total())

def load_cart(data: list[dict[str, float| int | str]]):
    for item in data:
        try:
            if 'discount' in item:
                a=DiscountedItem(item['name'], item['price'], item['discount'])
            else:
                b=Item(item['name'], item['price'])
                Cart.add(b)
        except ValueError as e:
            print(e)


    return Cart
        













