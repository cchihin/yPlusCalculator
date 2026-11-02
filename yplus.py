import numpy as np

rho = 1             # kg m^-3
U = 30               # m s^-1
L = 1                   # m
mu = 1. * 10**(-5)    # kg m^-1 s^-1
yp_desired = 1          # desired yplus
growth = 1.2

# Print params
print(f'--- Flow Parameters --- ')
print(f'rho:  {rho}     kg m^-3')
print(f'U:    {U}       m s^-1')
print(f'L:    {L}       m')
print(f'mu:   {mu:.2e}  kg m^-1 s^-1')

# Reynolds number
Re = rho * U * L / mu
print(f'Reynolds: {Re}')
print(f'--- Flow Parameters --- ')

# Calculate skin-friction Schlicting (eqn 21.16)
cf = (2 * np.log10(Re) - 0.65)**(-2.3)

# tau_w
tau_w = cf * 0.5 * rho * U**2
utau = np.sqrt(tau_w / rho)
y_min = yp_desired * mu / rho / utau
delta = 0.37 * L / Re**(0.2)        # Total BL height

# Compute the number of layers
nlayers = np.log( delta * (growth - 1) / y_min + 1 ) / np.log(growth)

print('')
print(f'--- Turbulent parameters --- ')
print(f'y+ (target): {yp_desired}')
print(f'y_min: {y_min} m')
print(f'Growth rate = {growth}')
print(f'delta = {delta}')
print(f'nLayers = {nlayers}')
print(f'Final layer height = {y_min * growth**nlayers}')
print(f'--- Turbulent parameters --- ')
