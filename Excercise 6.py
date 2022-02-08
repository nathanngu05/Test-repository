bike_hours = int(input("Hours spent bicycling: "))
swim_hours = int(input("Hours spent swimming: "))
jog_hours = int(input("Hours spent jogging: "))

bike_calories = bike_hours * 200
swim_calories = swim_hours * 275
jogging_calories = jog_hours * 475

total_calories = bike_calories + swim_calories + jogging_calories
weight_lost = total_calories / 7709
print(f"Total weight lost from exercise is {weight_lost:.3f} Kg")
