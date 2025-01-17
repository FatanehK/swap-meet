class Vendor:
    def __init__(self,inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    def get_by_category(self,category):
        list_category= []
        for item in self.inventory:
            if  item.category == category:
                list_category.append(item) 
        return list_category

    def swap_items(self,vendor,my_item,their_item):
        if their_item in vendor.inventory and my_item in self.inventory:
            vendor.remove(their_item)
            self.add(their_item)

            self.remove(my_item)
            vendor.add(my_item)
            return True
        
        return False

    def swap_first_item(self,vendor):
        if len(self.inventory) != 0 and len(vendor.inventory)!= 0 :
            temp_holding_item = self.inventory[0]
            self.inventory[0] = vendor.inventory[0]
            vendor.inventory[0] = temp_holding_item
            return True
        
        return False

    def get_best_by_category(self,category):
        # if self.inventory ==[]:
        #     return None
        # max_item = None
        # for item in self.inventory:
        #     if item.category == category:
        #         if max_item == None or item.condition > max_item.condition:
        #             max_item = item
        return max((item for item in self.inventory if item.category == category), key = lambda item: item.condition, default=None)
        


    def swap_best_by_category(self,other,my_priority,their_priority):
        others_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        return self.swap_items(other,my_best,others_best)


