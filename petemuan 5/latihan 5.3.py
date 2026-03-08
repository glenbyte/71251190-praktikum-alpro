celcius_to_fahrenheit = lambda C: (9/5) * C + 32
celcius_to_reamur = lambda C: 0.8 * C

C1 = 100
F1 = celcius_to_fahrenheit(C1)
print(f"Input C = {C1}")
print(f"Output F = {F1}")
print()

C2 = 80
R2 = celcius_to_reamur(C2)
print(f"Input C = {C2}")
print(f"Output R = {R2}")
print()

C3 = 0
F3 = celcius_to_fahrenheit(C3)
print(f"Input C = {C3}")
print(f"Output F = {F3}")