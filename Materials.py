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

    def __init__(self):


# MATERIALS

inconel_k_var = {100: 2.0, 200: 2.5, 300: 3.0}
inconel = Material(t_dependance=False, k=5, density=2.6)

al6061_k_var = {None}
al6061 = Material(t_dependance=False, k=3.0, density=1.0)

soot_k_var = {None}
soot = Material(t_dependance=False, k=1.0, density=1.0)  # TODO: Add the k of soot from soot document

materialDict = {"inconel": inconel, "al6061": al6061, "soot": soot}

# COOLANTS

# jetA = Coolant()

# Combustion Gas Heat Transfer Calculator

hG = None  # TODO: Define the hot gas heat transfer coefficient equation