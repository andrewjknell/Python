class store:
    def __init__(self, store_name):
        self.name = store_name
        self.product_list = []
    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self
    def sell_product(self, id):
        self.product_list.remove(self.product_list[id])
    def display_product(self):
        print(self.product_list)

safeway = store('Safeway')
sprouts = store('Sprouts')  

safeway.add_product('bread').add_product('cheese')
print(safeway.product_list)

class products:
    def __init__(self, product,category):
        self.name = products
        self.price = 0
        self.category = category  
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (percent_change/100)*self.price
        else:
            self.price -= (percent_change/100)*self.price
    def print_info(self):
        print(self.name, self.price, self.category)


