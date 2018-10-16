import Materials
import UserInputs

# The various geometry parameters that will be used to calculate thermal
# resistances. Refer to the attached image to see what the particular variable name
# refers to.

JH = 1
FW = 1
CW = 1
CH = 1
LH = 1
EW = 1
SH = 1
ETHCK = 1

# include the diameter at every point x in the engine? write a fn that returns the diameter based on
# x value


def rescalc(res, temp):

    if res == "RG":
        AG = ETHCK * CW * 0.5
        RG = 1 / (Materials.hG * AG)
        return RG
    elif res == "RS":
        LS = SH
        AS = EW * ETHCK
        KS = Materials.materialDict[UserInputs.coating_mat].k(temp)
        RS = LS / (KS*AS)
        return RS
    elif res == "R1":
        L1 = (LH + 0.5*CH)
        K1 = Materials.materialDict[UserInputs.liner_mat].k(temp)
        A1 = (0.5*FW) * ETHCK
        R1 = L1 / (K1 * A1)
        return R1
    elif res == "R2":
        L2 = LH
        K2 = Materials.materialDict[UserInputs.liner_mat].k(temp)
        A2 = (0.5*CW)*ETHCK
        R2 = L2 / (K2 * A2)
        return R2
    elif res == "R3":  # TODO: This is a coolant resistance and needs the coolant class defined
        A3 = (0.5*CW) * ETHCK
    elif res == "R4":  # TODO: This is a coolant resistance and needs the coolant class defined
        A4 = CH * ETHCK
    elif res == "R5":
        L5 = 0.25*FW
        K5 = Materials.materialDict[UserInputs.liner_mat].k(temp)
        A5 = CH*ETHCK
        R5 = L5 / (K5 * A5)
        return R5
    elif res == "R6":
        L6 = 0.5 * CH
        A6 = 0.5 * FW * ETHCK
        K6 = Materials.materialDict[UserInputs.liner_mat].k(temp)
        R6 = L6 / K6 * A6
    elif res == "R7":
        K7 = Materials.materialDict[UserInputs.jacket_mat].k(temp)
        L7 = JH
        A7 = 0.5 * FW * ETHCK
        R7 = L7 / K7 * A7
    elif res == "R8":
        H8 = UserInputs.air_coeff
        A8 = EW * ETHCK
        R8 = 1 / H8 * A8