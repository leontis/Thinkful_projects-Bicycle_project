def retail_price(whole_sale_price, shop_profit_margin,):
	retail_price = whole_sale_price*(1 + shop_profit_margin)
	return retail_price 

def wholesale_price(prod_cost, man_profit_margin,):
	whole_sale_price = prod_cost*(1 + man_profit_margin)
	return whole_sale_price 

class Wheel(object):
	"""A class for wheels"""
	def __init__(self, wheel_name, material):
		self.wheel_name = wheel_name
		self.material = material

	def	weight(self):
		if self.material in ["carbon", "aluminum", "steel"]:
			weight_dict = {"carbon": 5 ,"aluminum": 10 ,"steel": 15}
			return weight_dict[self.material]
		else: return None
	def	prod_cost(self):
		production_cost = {"carbon":100,"aluminum":50,"steel": 25}
		return production_cost[self.material]
 
class Frame(object):
	"""A class for frames"""
	def __init__(self, material):
		self.material = material
		
	def	weight(self):
		if self.material in ["carbon", "aluminum", "steel"]:
			weight_dict = {"carbon":15,"aluminum":25,"steel":35}
			return weight_dict[self.material]
		else: return None

	def	prod_cost(self):
		production_cost = {"carbon":200,"aluminum":100,"steel": 50}
		return production_cost[self.material]
		
class Bicycle_model(object):
	def __init__(self, name, frame, wheel, manufacturer):
		self.name = name
		self.manufacturer = manufacturer
		self.frame = frame
		self.wheel = wheel

	def total_wt(self):
		return self.frame.weight() + 2*self.wheel.weight()

	def prod_cost(self):
		return self.frame.prod_cost() + 2*self.wheel.prod_cost() 

class Manufacturer(object):
	
	def __init__(self,name,profit_margin):
		self.name = name
		self.profit_margin = profit_margin
		self.bicycle_models = []
		self.wholesale_price_list = {}

	def manufacture(self,model):
		self.bicycle_models.append(model)
		#print "Produced bicycle"
		self.wholesale_price
		return self.bicycle_models	

class Bike_shop(object):
	inventory = []
	def __init__(self,name, inventory, profit_margin):	
		self.name = name
		self.inventory = inventory
		self.profit_margin = profit_margin
	def purchase_stock(self,profit_margin,model,prod_cost,quantity):
		for i in range(0,quantity):
			self.inventory.append(model)
			wholesale_price = (1 + float(profit_margin))*prod_cost
			total_price = quantity*wholesale_price
		return wholesale_price, total_price

class Customer(object):
	bikes_owned = []
	def __init__(self,name,bike_fund,bikes_owned):
		self.name = name
		self.bike_fund = bike_fund	
		self.bikes_owned = bikes_owned
	def afford(self,bicycle_model):	
		if bicycle_model.retail < self.bike_fund:
			can_afford = True
		else: can_afford = False
		return can_afford	
	def purchase_bike(self,bicycle_model):
		if 	bicycle_model.retail < self.bike_fund:
			self.bike_fund = self.bike_fund - bicycle_model.retail
			self.bikes_owned.append(bicycle_model.name)
			return "Purchase successful"
		else:
			return "Purchase not successful"
	def own_bike(self): 
		if bikes_owned == []:
			return False
		else:
			return True	
		