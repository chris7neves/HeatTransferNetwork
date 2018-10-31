### MAKE SURE ALL QUANTITIES ARE IN IMPERIAL ###

# To define material properties, go to "Materials.py"

liner_mat = "inconel"
coating_mat = "soot"
jacket_mat = "al6061"
coolant = "jetA"

# To define material properties, go to "Materials.py"

coolant_flowrate = 3.3  # lb/sec
num_channels = 96
air_coeff = 10.0  # Enter the h of ambient air. This is a user input to acomodate imperial or metric units.
nozzleinlet_temp = 6390  # Rankine
nozzleinlet_pressure = 375  # Psia
c_star = 5820.86  # From CEA - ft/s
gamma = 1.14  # From CEA
cp_gas = 0.804
throat_dia = 3.79
throat_rad_curvature = 0.5
combustion_gas_molecular_weight = 22.5  # In lb/mol for imperial
mach_number_inlet = 1.14

chamber_mach_number = 0.0
throat_mach_number = 1.00  # Is the Mach number for the throat only 1 value?
nozzle_mach_number = 2.624  # Is the Mach number for the nozzle only 1 value?




