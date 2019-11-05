from django.test import TestCase

from .untils import SolverMethods

# Create your tests here.
class TestCalcMethods(TestCase):        
    def TestShortLine(self):
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

        short_line_resolve = {
            "V1":(502656.4209149348+4154.870250369401j),
            "I1":(129.904-55.338872268957566j)
        }

        self.assertEqual(short_line, short_line_resolve)

    def TestExponentialModel(self):
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

        exponential_model = SolverMethods(line_params).exponential_model()

        exponential_model_resolve = {
            'V1': (499965.10710945376+4598.091431398168j), 
            'I1': (129.20928871564678+100.85196742299863j)
        }

        self.assertEqual(exponential_model, exponential_model_resolve)

    def TestHyperbolicModel(self):
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

            hyperbolic_model = SolverMethods(line_params).hyperbolic_model()

            hyperbolic_model_resolve = {
                'V1': (499965.1071094539+4598.0914313981675j), 
                'I1': (129.20928871564695+100.85196742299864j)
            }

            self.assertEqual(hyperbolic_model, hyperbolic_model_resolve)

    def TestLineModelT(self):
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

            line_model_t = SolverMethods(line_params).line_model_t()

            line_model_t_resolve = {
                'V1': (499959.7599515653+4595.572249452116j), 
                'I1': (129.25560662315544+101.13190621422038j)
            }

            self.assertEqual(line_model_t, line_model_t_resolve)

    def TestLineModelPi(self):
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

            line_model_pi = SolverMethods(line_params).line_model_pi()

            line_model_pi_resolve = {
                'V1': (499968.77196072444+4605.54190851693j), 
                'I1': (129.18527650436332+100.71248185769849j)
            }

            self.assertEqual(line_model_pi, line_model_pi_resolve)