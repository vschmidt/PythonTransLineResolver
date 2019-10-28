"""
    *All variables respect SI system, American system causes student cancer and suicide
    *All imaginary variables must be in rectangular coordinates
"""

import math, cmath

class Line():
    def __init__(self):
        def p2_solver(power_factor, S2):
            p2 = power_factor * S2
            return p2

        def q2_solver(p2, s2):
            q2 = math.sqrt(s2**2 - p2**2)
            return q2

        self.R = 0.000072197 #In Ω/m
        self.G = 0 #In S/m
        self.L = 0.000001142090 #In Henry/m
        self.C = 0.0000000000103488 #In Farads/m
        self.l = 80000 #In meters            
        
        self.num_phases = 1 #1 or 3
        self.power_factor = 0.92 #cos(Φ) inductive
        self.V2 = 500000 #In Volts
        self.f = 60 #In Hertz

        self.S2 = 70600000 #In VA
        self.P2 = p2_solver(self.power_factor, self.S2) #In W
        self.Q2 = q2_solver(self.P2, self.S2) #In VAr
        self.S2COMPL = complex(self.P2, self.Q2) #In VA

        self.XL = 2 * math.pi * self.f * self.L #In Ω 
        self.B = 2 * math.pi * self.f * self.C #In Ω 
        
        self.Z = complex(self.R, self.XL) #In VA
        self.Y = complex(self.G, self.B) #In VA
        self.ZC = cmath.sqrt(self.Z/self.Y) #In Ω
        self.GAMA = cmath.sqrt(self.Z * self.Y) #In 1/m 
        self.ALPHA = self.GAMA.real #In nep/m 
        self.BETA = self.GAMA.imag #In rad/m
        
        self.GAMAX = self.GAMA * self.l
        self.w = 2 * math.pi * self.f
        self.v = self.w / self.BETA
        self.videal = 1 / math.sqrt(self.L * self.C)
        self.t = self.v / self.l

        self.I2 = (self.S2COMPL / self.V2).conjugate()      

class SolverMethods(Line):
    
    def short_line(self):
        V1 = self.V2 + self.I2 * self.Z * self.l
        I2 = self.I2

        return {
            "V1":V1,
            "I2":I2,
            }

if __name__ == "__main__":
    print("Init")
    
