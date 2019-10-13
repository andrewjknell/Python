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