# PythonTransLineResolver

Transmission Line Parameter Resolution Algorithm

This Python library provides algorithms for resolving transmission line parameters using various mathematical models. It's designed to assist electrical engineers and students in power system analysis.

## Features

- **Multiple Solution Methods**: Implement different transmission line models
- **Comprehensive Parameter Calculation**: Calculate impedance, admittance, and propagation constants
- **Power Flow Analysis**: Solve for voltage and current at line terminals
- **SI Unit Support**: All calculations use the International System of Units

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/PythonTransLineResolver.git
cd PythonTransLineResolver
```

## Quick Start

```python
# Define transmission line parameters
line_params = {
    "R": 0.000072197,      # Resistance (Ω/m)
    "G": 0,                # Conductance (S/m)
    "L": 0.000001142090,   # Inductance (H/m)
    "C": 0.0000000000103488, # Capacitance (F/m)
    "l": 80000,            # Length (m)
    "power_factor": 0.92,  # Power factor
    "V2": 500000,          # Receiving end voltage (V)
    "f": 60,               # Frequency (Hz)
    "S2": 70600000         # Apparent power (VA)
}
```

```bash
# Run with your favorive python 3.x version
python main.py
```


## Available Methods

### 1. Short Line Model
Simple model for short transmission lines where line parameters are lumped.

### 2. Exponential Model
Exact solution using exponential functions for distributed parameter analysis.

### 3. Hyperbolic Model
Alternative exact solution using hyperbolic functions.

### 4. T-Model
Pi-equivalent circuit representation with T-configuration.

### 5. Pi-Model
Pi-equivalent circuit representation with Pi-configuration.

**Properties:**
- `R`: Resistance (Ω/m)
- `G`: Conductance (S/m)
- `L`: Inductance (H/m)
- `C`: Capacitance (F/m)
- `l`: Line length (m)
- `power_factor`: Power factor (cos φ)
- `V2`: Receiving end voltage (V)
- `f`: Frequency (Hz)
- `S2`: Apparent power (VA)

**Calculated Properties:**
- `Z`: Series impedance (Ω)
- `Y`: Shunt admittance (S)
- `ZC`: Characteristic impedance (Ω)
- `GAMA`: Propagation constant (1/m)
- `ALPHA`: Attenuation constant (Np/m)
- `BETA`: Phase constant (rad/m)

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this library in your research, please cite:

```
PythonTransLineResolver. (Year). Transmission Line Parameter Resolution Algorithm. 
Retrieved from https://github.com/vschmidt/PythonTransLineResolver
```
