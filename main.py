"""
    *All variables respect SI system, American system causes student cancer and suicide
    *All imaginary variables must be in rectangular coordinates
"""

import math, cmath

class Line():
    def __init__(self, line):
        def p2_solver(power_factor, S2):
            p2 = power_factor * S2
            return p2

        def q2_solver(p2, s2):
            q2 = math.sqrt(s2**2 - p2**2)
            return q2

        self.R = line["R"] 
        self.G = line["G"] 
        self.L = line["L"] 
        self.C = line["C"] 
        self.l = line["l"]          
        
        self.num_phases = 1 #1 or 3
        self.power_factor = line["power_factor"]
        self.V2 = line["V2"]
        self.f = line["f"]

        self.S2 = line["S2"]
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
        I1 = self.I2

        return {
            "V1":V1,
            "I1":I1
            }

    def exponential_model(self):
        V1 = (((self.V2+self.I2*self.ZC)/2)*cmath.exp(self.GAMAX)) + (((self.V2-self.I2*self.ZC)/2)*cmath.exp(-self.GAMAX))
        I1 = (1/self.ZC)*((((self.V2+self.I2*self.ZC)/2)*cmath.exp(self.GAMAX))-(((self.V2-self.I2*self.ZC)/2)*cmath.exp(-self.GAMAX)))

        return {
            "V1":V1,
            "I1":I1
            }

    def hyperbolic_model(self):
        h_sin = cmath.sinh(self.GAMAX)     
        h_cos = cmath.cosh(self.GAMAX)

        V1 = self.V2*(h_cos) + self.I2*self.ZC*h_sin
        I1 = self.I2*(h_cos) + (self.V2/self.ZC)*h_sin

        return{
            "V1":V1,
            "I1":I1
        }

    def line_model_t(self):
        V1 = self.V2*(1+(self.Z*self.Y*(self.l**2))/2)+self.I2*self.Z*self.l*(1+(self.Z*self.Y*(self.l**2))/4)
        I1 = self.I2*(1+(self.Z*self.Y*(self.l**2))/2)+self.V2*self.Y*self.l
        return{
            "V1":V1,
            "I1":I1
        }
    
    def line_model_pi(self):
        V1 = self.V2*(1+(self.Z*self.Y*(self.l**2))/2)+self.I2*self.Z*self.l
        I1 = self.I2*(1+(self.Z*self.Y*(self.l**2))/2)+self.V2*self.Y*self.l*(1+(self.Z*self.Y*(self.l**2))/4)
        return{
            "V1":V1,
            "I1":I1
        }
    
if __name__ == "__main__":

    line_params = {
        "R": 0.000072197,#In Ω
        "G": 0, #In S/m
        "L": 0.000001142090, #In Henry/m
        "C": 0.0000000000103488, #In Farads/m
        "l": 80000, #In meters            
        "power_factor": 0.92, #cos(Φ) inductive
        "V2": 500000, #In Volts
        "f": 60, #In Hertz
        "S2": 70600000 #In VA
    }

    short_line = SolverMethods(line_params).short_line()
    exponential_model = SolverMethods(line_params).exponential_model()
    hyperbolic_model = SolverMethods(line_params).hyperbolic_model()
    line_model_t = SolverMethods(line_params).line_model_t()
    line_model_pi = SolverMethods(line_params).line_model_pi()

    print("Method: Short Line")
    print("Input Voltage: "+str(short_line["V1"])+"[V]")
    print("Input Courent: "+str(short_line["I1"])+"[A]")
    print("")
    
    print("Method: Exponential")
    print("Input Voltage: "+str(exponential_model["V1"])+"[V]")
    print("Input Courent: "+str(exponential_model["I1"])+"[A]")
    print("")

    print("Method: Hyperbolic")
    print("Input Voltage: "+str(hyperbolic_model["V1"])+"[V]")
    print("Input Courent: "+str(hyperbolic_model["I1"])+"[A]")
    print("")
    
    print("Method: T-Line")
    print("Input Voltage: "+str(line_model_t["V1"])+"[V]")
    print("Input Courent: "+str(line_model_t["I1"])+"[A]")
    print("")

    print("Method: Pi-Line")
    print("Input Voltage: "+str(line_model_pi["V1"])+"[V]")
    print("Input Courent: "+str(line_model_pi["I1"])+"[A]")

