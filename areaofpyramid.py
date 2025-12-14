length = float(input("Enter the length of the base: "))

slant_height = 5   # fixed slant height

base_area = length * length
lateral_area = 2 * length * slant_height

total_area = base_area + lateral_area

print("Area of the pyramid is:", total_area)
