class Wheel(object):
	"""A class for wheels"""
	def __init__(self,model_name,weight,production_cost):
		self.model_name = model_name
		self.weight = weight
		self.production_cost = production_cost

class Frames(object):
	"""A class for frames"""
	def __init__(self,material,weight,production_cost):
		self.material = material
		self.weight = weight
		self.production_cost = production_cost
		
class Bicycle_models(object):
	def __init__(self,name,manufacturer,total_wt,total_cost,components):
		self.name = name
		self.manufacturer = manufacturer
		self.total_wt = total_wt
		self.total_cost = total_cost
		self.components = components

class Manufacturer(object):
	def __init__(self,name,models,profit_margin):
		self.name = name
		self.models = models
		self.profit_margin = profit_margin

class Bike_shops(object):
	def __init__(self,name,inventory,profit_margin):	
		self.name = name
		self.inventory = inventory
		self.profit_margin = profit_margin

class Customers(object):
	def __init__(self,name,bike_fund):
		self.name = name
		self.bike_fund = bike_fund		
		
		

