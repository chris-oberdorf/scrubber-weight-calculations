# constants
INCH_TO_MM = 25.4
MM3_TO_L = 1.0e-6
L_TO_GAL = 1 / 3.785
KG_TO_LBS = 2.205

# inputs
length = 4  # in feet
width = 4  # in feet
depth = 2.5  # in mm
coverage = 0.85  # amount [0-1]
num_runs = 1.5

# convert to mm
length = length * INCH_TO_MM
width = width * INCH_TO_MM

# find area
area = length * width
area *= coverage

# find volume
volume_l = area * depth
volume_l *= MM3_TO_L
volume_l *= num_runs

# volume in gallons
volume_gal = volume_l * L_TO_GAL

# weight
weight_kg = volume_l
weight_lb = weight_kg * KG_TO_LBS

print(f"The volume is {volume_l} liters / {volume_gal} gallons.")
print(f"The weight is {weight_kg} kg / {weight_lb} lbs.")
