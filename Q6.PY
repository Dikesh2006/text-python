


cities = ["Bhopal", "Indore", "Delhi", "Mumbai",
          "Pune", "Jaipur", "Chennai", "Kolkata"]


print("First 4 Cities:", cities[:4])


print("Last 4 Cities:", cities[-4:])


cities.append("Hyderabad")
print("After Adding City:", cities)


cities.pop(0)
print("After Removing First City:", cities)


city_tuple = tuple(cities)
print("Tuple:", city_tuple)