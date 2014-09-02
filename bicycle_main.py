from classes import *
inventory = []
shop1 = Bike_shop("Some_Great_Bikes", inventory, .20)

cust1 = Customer("Kevin",1000,[])
cust2 = Customer("Craig",300,[])
cust3 = Customer("Neocles",150,[])
customers = [cust1, cust2, cust3]
print "\nCustomers: \n" 
for cust in customers:
	print "Name :", cust.name, "/ Funds: ", cust.bike_fund

frame1 = Frame("carbon")
frame2 = Frame("aluminum")
frame3 = Frame("steel")

frames = [frame1,frame2,frame3]
print "\nFrames: \n" 
for frame in frames:
	print frame.material, "frame weight: ", frame.weight(), "frame cost: ", frame.prod_cost()

wheel1 = Wheel("Sleek","carbon")
wheel2 = Wheel("OK","aluminum")
wheel3 = Wheel("Clunky","steel")

wheels = [wheel1, wheel2, wheel3]
print "\nWheels: \n" 
for wheel in wheels:
	print wheel.wheel_name, "wheel weight: ", wheel.weight(), "wheel cost: ", wheel.prod_cost()

man1 = Manufacturer("Cheap_Bikes",0.05)
man2 = Manufacturer("Pricy_Bikes",0.25)
manufacturers = [man1, man2]

print "\nManufacturers: \n" 
for man in manufacturers:
	print "Name :", man.name, "/ Margin = ", man.profit_margin

model1 = Bicycle_model("Swift", frame1, wheel1, man1)
model2 = Bicycle_model("JustSo", frame2, wheel2, man1)
model3 = Bicycle_model("Clunker", frame3, wheel3, man1)
model4 = Bicycle_model("Swift", frame1, wheel1, man2)
model5 = Bicycle_model("JustSo", frame2, wheel2, man2)
model6 = Bicycle_model("Clunker", frame3, wheel3, man2)


models = [model1, model2, model3, model4, model5, model6]

print "\nModels: \n" 
for model in models:
	 whole_sale = wholesale_price(model.prod_cost(),model.manufacturer.profit_margin)
	 retail = retail_price(whole_sale, shop1.profit_margin)
	 print model.name, model.manufacturer.name, "wt =", model.total_wt(), "prod cost = $",model.prod_cost(), "whole_sale = $", whole_sale, "retail= $", retail

for man in manufacturers:
	for model in models:
		shop1.purchase_stock(man.profit_margin, model, model.prod_cost(), 1)

for index in range(0,len(shop1.inventory)):
	print "Manuf. = ", shop1.inventory[index].manufacturer.name, "\t Model = ",shop1.inventory[index].name

for cust in customers:
	for model in models:
		whole_sale = wholesale_price(model.prod_cost(),model.manufacturer.profit_margin)
		retail = retail_price(whole_sale, shop1.profit_margin)
		model.retail = retail
		print cust.name, "\t",cust.bike_fund, "\t", model.name, "\t","$",retail, cust.afford(model),"\n"

