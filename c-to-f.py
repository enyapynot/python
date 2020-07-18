Celsius=0.0
Fahrenheit=0.0
celsius=0.0
fahrenheit=0.0

def convert_to_farenheit(celsius):
  fahrenheit = 9.0/5.0 * float(celsius) + 32
  return fahrenheit
  
Celsius = input("Pass the world\'s unit of temperature \(C\). You\'ll get the USA unit \(F\)")
print("The weird USA temperature is ", convert_to_farenheit(Celsius), " F, Which is " , Celsius, " degrees C")
