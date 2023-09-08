fahr = input("enter a temperature in degrees fahrenheit: ")
fahr = int(fahr)
celsius = (fahr - 32)*(5/9)
celsius = float(celsius)
celsius = celsius - (celsius%0.01)

print("that is",celsius,"degrees celsius")