import Materials
import UserInputs
import ResistanceDef
import ConvergenceCheck

####  FILL OUT BEFORE RUNNING SIMULATION ####
g = 32.2  # Gravitational Acceleration
dia = 3.79  # Radius at point of interest
engineaxis_temp = 5889.6  # Temperature at the point along the engine axis of interest.
iterations = 1000  # Maximum number of iterations
analysis_location = "throat"  # Can be "chamber", "throat", "nozzle"
# Constant Temps #
tg = 5889.6
tcoolant = 761.67
tinf = 528.67
# Initial Guesses #
ts = 1391
twg = 1391
tcw1 = 1391
tcw2 = 1391
tf = 1391
tow = 1391
tj = 1391
#############################################

if analysis_location == "chamber":

elif analysis_location == "throat":

elif analysis_location == "nozzle":

else:
    print("The analysis location was either not specified or incorrect.\n")




#  TODO: Coolant temperatures need to be defined for the engine length.
def hG(temp_ts, location):  # The combustion temperature along the engine axis at the point that is being analyzed should be passed to this along with soot temperature temp_ts.
    if location == "throat":  # I think the formula for Pc ns only needs the mach number at the nozzle inlet, so the chamber mach number.
        mach_number = UserInputs.throat_mach_number
    elif location == "nozzle":
        mach_number = UserInputs.nozzle_mach_number
    elif location == "chamber":
        mach_number = UserInputs.chamber_mach_number
    else:
        print("Error in hG. The location that hG is to be found is not specified. Assuming chamber.")
        mach_number = UserInputs.chamber_mach_number

    area = 0.25 * (dia ** 2)
    area_throat = 0.25 * (UserInputs.throat_dia ** 2)
    prandlt = (4 * UserInputs.gamma) / (9 * UserInputs.gamma - 5)
    gas_viscosity = (46.6 * (10 ** (-10))) * (UserInputs.combustion_gas_molecular_weight ** 0.5) * (tg ** 0.6)
    pc_ns = UserInputs.nozzleinlet_pressure * ((1 + (0.5 * (UserInputs.gamma - 1) * (UserInputs.mach_number_inlet ** 2))) ** (UserInputs.gamma / (UserInputs.gamma - 1)))
    tc_ns = UserInputs.nozzleinlet_temp * (1 + (0.5 * (UserInputs.gamma - 1) * (UserInputs.mach_number_inlet ** 2)))  # Im pretty sure this can be replaced by temp_combustion

    term_1 = 0.026 * (1 / (UserInputs.throat_dia ** 0.2))
    term_2 = ((gas_viscosity ** 0.2) * UserInputs.cp_gas) / (prandlt ** 0.6)
    term_3 = ((pc_ns * g) / UserInputs.c_star) ** 0.8
    term_4 = (UserInputs.throat_dia / UserInputs.throat_rad_curvature) ** 0.1
    term_5 = (area_throat / area) ** 0.9
    sigma_t_1 = 0.5 * (temp_ts / tc_ns)  # In this case, ts is the temperature before the wall.
    sigma_t_2 = (1 + (0.5 * (UserInputs.gamma - 1) * (mach_number ** 2)))
    sigma_denom = (((sigma_t_1 * sigma_t_2) + 0.5) ** 0.68) * (sigma_t_2 ** 0.12)
    sigma = 1 / sigma_denom

    hG_gases = term_1 * term_2 * term_3 * term_4 * term_5 * sigma

    return hG_gases

####  Main Loop  ####
error = 1

for i in range(1, iterations):
    if error > 0.01:
        HG = hG(ts, analysis_location)

        tsp = ts
        ts = ( ( (1/ ResistanceDef.rg(HG)) + (1 / ResistanceDef.rs(ts)) ) ** -1 ) * ( (tg / ResistanceDef.rg(HG)) + (twg / ResistanceDef.rs(ts)) )

        twgp = twg
        twg = (((1 / ResistanceDef.r1(twg)) + (1 / ResistanceDef.rs(ts)) + (1 / ResistanceDef.r2(twg)) ) ** -1) * ((tf / ResistanceDef.r1(twg)) + (tcw1 / ResistanceDef.r2(twg)) + (ts / ResistanceDef.rs(ts)))

        tcw1p = tcw1
        tcw1 = ( ( (1/ ResistanceDef.r2(twg)) + (1 / ResistanceDef.r3(tcoolant, tcw1)) ) ** -1 ) * ( (twg / ResistanceDef.r2(twg)) + (tcoolant / ResistanceDef.r3(tcoolant, tcw1)) )

        tcw2p = tcw2
        tcw2 = ( ( (1/ ResistanceDef.r4(tcoolant, tcw2)) + (1 / ResistanceDef.r5(tf)) ) ** -1 ) * ( (tcoolant / ResistanceDef.r4(tcoolant, tcw2)) + (tf / ResistanceDef.r5(tf)) )

        tfp = tf
        tf = (((1 / ResistanceDef.r1(twg)) + (1 / ResistanceDef.r6(tf)) + (1 / ResistanceDef.r5(tf)) ) ** -1) * ((twg / ResistanceDef.r1(twg)) + (tow / ResistanceDef.r6(tf)) + (tcw2 / ResistanceDef.r5(tf)))

        towp = tow
        tow = ( ( (1/ ResistanceDef.r7(tow)) + (1 / ResistanceDef.r6(tf)) ) ** -1 ) * ( (tj / ResistanceDef.r7(tow)) + (tf / ResistanceDef.r6(tf)) )

        tjp = tj
        tj = ( ( (1/ ResistanceDef.r7(tow)) + (1 / ResistanceDef.R8) ) ** -1 ) * ( (tow / ResistanceDef.r7(tow)) + (tinf / ResistanceDef.R8) )

        error = ConvergenceCheck.frobenius_norm(tsp, ts, twgp, twg, tcw1p, tcw1, tcw2p, tcw2, tfp, tf, towp, tow, tjp, tj)
    else:
        break

print("Iterations: ", i)
print("Error: ", error)
print("Hg: ", HG)
print("Ts: ", ts)
print("Twg: ", twg)
print("Tcw1: ", tcw1)
print("Tcw2: ", tcw2)
print("Tf: ", tf)
print("Tow: ", tow)
print("Tj: ", tj)