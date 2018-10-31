import UserInputs
import ResistanceDef
# Contains structures of each material containing
# their physical properties and methods in order to
# return their h or k values.


class Material:  # IMPORTANT: Make sure to accurately assign t_dependance and k!

    def __init__(self, t_dependance, k, density):
        self.t_dependance = t_dependance
        self.__k = k
        self.density = density
        self.kFinal = None

    def k(self, temp=None):  # class function that assigns the k conductivity. Based on if its temp dependant or not
        if not self.t_dependance:
            return self.__k
        else:
            for t in self.__k:
                if temp >= t:
                    self.kFinal = self.__k[t]
            return self.kFinal


class Coolant:

    def __init__(self, viscosity_coolant, cp_coolant, k_coolant):
        self.viscosity_coolant = viscosity_coolant
        self.cp_coolant = cp_coolant
        self.k_coolant = k_coolant
        self.d = (ResistanceDef.CW * ResistanceDef.CH) / (ResistanceDef.CW + ResistanceDef.CH)

    def c_viscosity(self, temp=None):  # Should also add option to calculate viscosity using molar mass and temp.
        tempvisc = None
        for t in self.viscosity_coolant:
            if temp >= t:
                tempvisc = self.viscosity_coolant[t]
        return tempvisc

    def c_cp(self, temp=None):
        tempcp = None
        for t in self.cp_coolant:
            if temp >= t:
                tempcp = self.cp_coolant[t]
        return tempcp

    def c_k(self, temp=None):
        tempk = None
        for t in self.k_coolant:
            if t >= temp:
                tempk = self.k_coolant[t]
        return tempk

    def h_coolant(self, t_wall, t_bulk):
        Pr = (self.c_viscosity(t_bulk) * self.c_cp(t_bulk)) / self.c_k(t_bulk)
        G = UserInputs.coolant_flowrate / (UserInputs.num_channels * ResistanceDef.CH * ResistanceDef.CW)
        term1 = (0.029 * self.c_cp(t_bulk) * (self.c_viscosity(t_bulk) ** 0.2)) / (Pr ** (2/3))
        term2 = (G ** 0.8) / (self.d ** 0.2)
        term3 = (t_bulk / t_wall) ** 0.55
        h_coolant = term1 * term2 * term3
        return h_coolant


# MATERIALS

inconel_k_var = {100: 2.0, 200: 2.5, 300: 3.0}
inconel = Material(t_dependance=False, k=5, density=2.6)

al6061_k_var = {None}
al6061 = Material(t_dependance=False, k=3.0, density=1.0)

soot_k_var = {None}
soot = Material(t_dependance=False, k=0.000007, density=1.0)  # Units of soot here are BTU/(in. Sec F). Check the bible to see if ok

materialDict = {"inconel": inconel, "al6061": al6061, "soot": soot}

# COOLANTS

jetA_k_var = {100: 80, 200: 90, 5000: 100}
jetA_cp_var = {100: 0.004, 200: 0.005, 5000: 0.006}
jetA_visc_var = {100: 0.000004, 200: 0.000005, 5000: 0.000006}  # viscosity in lb/in-s
jetA = Coolant(viscosity_coolant=jetA_visc_var, cp_coolant=jetA_cp_var, k_coolant=jetA_k_var)

coolantdict = {"jetA": jetA}



