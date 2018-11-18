### MAKE SURE ALL QUANTITIES ARE IN IMPERIAL ###

# To define material properties, go to "Materials.py"

liner_mat = "c18150"
coating_mat = "soot"
jacket_mat = "al6061"
coolant = "jetA"

# To define material properties, go to "Materials.py"

coolant_flowrate = 3.3  # lb/sec
num_channels = 96
air_coeff = 0.00000355  # Btu/in^2-s-R
nozzleinlet_temp = 6390  # Rankine
nozzleinlet_pressure = 375  # Psi
c_star = 5869.422  # From CEA - ft/s
gamma = 1.14  # From CEA
# cp_gas = 0.804  # Btu/lb-R
throat_dia = 3.79  # inches
throat_rad_curvature = 0.5  # inches
combustion_gas_molecular_weight = 22.5  # In lb/mol

mach_number_inlet = 1.14
chamber_mach_number = 0.0
throat_mach_number = 1.00  # Is the Mach number for the throat only 1 value?
nozzle_mach_number = 2.624  # Is the Mach number for the nozzle only 1 value?




