import Materials
import UserInputs

# The various geometry parameters that will be used to calculate thermal
# resistances. Refer to the attached image to see what the particular variable name
# refers to.

JH = 0.609705
FW = 0.02952756  # Check actual fin thickness
CW = 0.02952756
CH = 0.177165
LH = 0.06212998
EW = 0.0590551
SH = 0.001
ETHCK = 0.5


# RG
def rg(hg):
    AG = ETHCK * CW * 0.5
    RG = 1 / (hg * AG)
    return RG


# RS
def rs(ts):
    LS = SH
    AS = EW * ETHCK
    KS = Materials.materialDict[UserInputs.coating_mat].k(ts)
    RS = LS / (KS*AS)
    return RS


# R1
def r1(twg):
    L1 = (LH + 0.5*CH)
    K1 = Materials.materialDict[UserInputs.liner_mat].k(twg)
    A1 = (0.5*FW) * ETHCK
    R1 = L1 / (K1 * A1)
    return R1


# R2
def r2(twg):
    L2 = LH
    K2 = Materials.materialDict[UserInputs.liner_mat].k(twg)
    A2 = (0.5*CW)*ETHCK
    R2 = L2 / (K2 * A2)
    return R2


# R3
def r3(tc, tcw1):
    H3 = Materials.coolantdict[UserInputs.coolant].h_coolant(tcw1, tc)
    A3 = (0.5*CW) * ETHCK
    R3 = 1 / (H3 * A3)
    return R3


# R4
def r4(tc, tcw2):
    H4 = Materials.coolantdict[UserInputs.coolant].h_coolant(tcw2, tc)
    A4 = CH * ETHCK
    R4 = 1 / (H4 * A4)
    return R4


# R5
def r5(tf):
    L5 = 0.25*FW
    K5 = Materials.materialDict[UserInputs.liner_mat].k(tf)
    A5 = CH*ETHCK
    R5 = L5 / (K5 * A5)
    return R5


# R6
def r6(tf):
    L6 = 0.5 * CH
    A6 = 0.5 * FW * ETHCK
    K6 = Materials.materialDict[UserInputs.liner_mat].k(tf)
    R6 = L6 / K6 * A6
    return R6


# R7
def r7(tow):
    K7 = Materials.materialDict[UserInputs.jacket_mat].k(tow)
    L7 = JH
    A7 = 0.5 * FW * ETHCK
    R7 = L7 / K7 * A7
    return R7

# R8
H8 = UserInputs.air_coeff
A8 = EW * ETHCK
R8 = 1 / H8 * A8
