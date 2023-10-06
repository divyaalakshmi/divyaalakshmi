first_name="coco"
last_name="theco"
print(type(first_name))
print(type(last_name))
#build a menu
title ="menu".upper()
print(title.center(20,"="))
print("coffee".ljust(16,"=")+"$1".rjust(4))
print("muffin".ljust(16,"=")+"$2".rjust(4))
print("cheesecake".ljust(16,"=")+"$3".rjust(4))

#string index values
first_name="coco"
last_name="theco"
print(first_name[1])
print(first_name[1])
print(first_name[1:-1])

# some methods return boolean data
print(first_name.startswith("c"))
print(last_name.endswith("q"))
# boolean data type
my_value=True
x=bool(False)
print(type(x))
print(isinstance(my_value,bool))
#numeric data types
#integer type
price=100
best_price=int(80)
print(type(price))
print(isinstance(best_price,int))
# complex type
comp_value=1+2j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
# built-in value
cgp=8.01
print(abs(cgp))
print(abs(cgp+-1))
print(round(cgp))
print(round(cgp,1))
import math
print(math.pi)
print(math.floor(cgp))
print(math.ceil(cgp))
# casting a number to integer
zipcode="1001"
zip_value=int(zipcode)
print(type(zip_value))
# error if yo attempt
#zip_value= int("new_york")

               