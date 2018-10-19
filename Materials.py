import UserInputs
import ResistanceDef
# Contains structures of each material containing
# their physical properties and methods in order to
# return their h or k values.


class Material: # IMPORTANT: Make sure to accurately assign t_dependance and k!

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

# TODO: Finish coolant class


class Coolant:

    fuelflow = UserInputs.coolant_flowrate

    def __init__(self, t_dependance_cp, t_dependance_v, viscosity_coolant, cp_coolant, k_coolant):
        self.t_dependance_v = t_dependance_v
        self.t_dependance_cp = t_dependance_cp

        if self.t_dependance_cp: # TODO: Define this temperature variation along with the viscosity one

        else:
            self.cp_coolant = cp_coolant

        self.viscosity_coolant = viscosity_coolant
        self.cp_coolant = cp_coolant
        self.k_coolant = k_coolant
        self.hydraulic_dia = self.d()

    def d(self):
        d = (UserInputs.CW * UserInputs.CH) / (UserInputs.CW + UserInputs.CH)
        return d

    def h_coolant(self, t_wall, t_bulk):
        Pr = (self.viscosity_coolant * self.cp_coolant) / self.k_coolant
        G = UserInputs.coolant_flowrate / (UserInputs.num_channels * ResistanceDef.CH * ResistanceDef.CW)
        term1 = (0.029 * self.cp_coolant * (self.viscosity_coolant ** 0.2)) / (Pr ** (2/3))
        term2 = (G ** 0.8) / (self.hydraulic_dia ** 0.2)
        term3 = (t_bulk / t_wall) ** 0.55
        h_coolant = term1 * term2 * term3
        return h_coolant



# MATERIALS

inconel_k_var = {100: 2.0, 200: 2.5, 300: 3.0}
inconel = Material(t_dependance=False, k=5, density=2.6)

al6061_k_var = {None}
al6061 = Material(t_dependance=False, k=3.0, density=1.0)

soot_k_var = {None}
soot = Material(t_dependance=False, k=1.0, density=1.0)  # TODO: Add the k of soot from soot document

materialDict = {"inconel": inconel, "al6061": al6061, "soot": soot}

# COOLANTS

# TODO: Create coolant dictionnary and add jet-A as a coolant

# jetA = Coolant()

# Combustion Gas Heat Transfer Calculator


