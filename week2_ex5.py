class ShoppingCart:
    def __init__(self, customer_name : str, discount_code:str):
        self._customer_name = customer_name
        self.__discount_code = discount_code
        self._items = {}

    @property
    def customer_name(self):
        return self._customer_name

    def add_item(self, name, price, quantity):
        if price < 0:
            raise ValueError('price must be positive')
        if quantity < 0 or type(quantity) != int:
            raise ValueError('quantity must be a positive integer')
        if name not in self._items:
            self._items[name] = {
                'price': price,
                'quantity': quantity
            }
        else:
            self._items[name]['quantity'] += quantity
    def remove_item(self, name):
        if name not in self._items:
            raise ValueError('item not found')
        del self._items[name]
    @property
    def item_count(self):
        # total = 0
        # for item in self._items.values():
        #     total += item['quantity']
        # return total
        return sum(item['quantity'] for item in self._items.values())
    @property
    def subtotal(self):
        res = 0
        for item in self._items.values():
            res += item['price'] * item['quantity']
        return round(res, 2)
        # return round(sum(item['price'] * item['quantity'] for item in self._items.values()), 2)
        # return round(sum(item['price'] * item['quantity'] for item in self._items.values()), 2)

    def apply_discount(self, code):
        if code != self.__discount_code:
            raise ValueError('invalid discount code')
        if self._discount_applied:
            raise ValueError('discount already applied')
        self._discount_applied = True
    @property
    def total(self):
        if self._discount_applied:
            return round(self.subtotal * 0.9, 2)
        else:
            return self.subtotal


        
