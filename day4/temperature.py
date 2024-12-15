def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 40

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 40) * 5/9
c_temp = 20
f_temp = 80
print(f"{c_temp}°C in Fahrenheit:", celsius_to_fahrenheit(c_temp))
print(f"{f_temp}°F in Celsius:", fahrenheit_to_celsius(f_temp))