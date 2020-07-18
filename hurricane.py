windspeed = eval(input("In mph, how hard is she blowing! : "))

if windspeed <= 73:
    print(windspeed, "mph Is just a light breeze. Hardly a hurricane.")
    
elif windspeed >= 74 and windspeed <= 95:
    print(windspeed, "mph Is a Category 1 hurricane")
    
elif windspeed >= 96 and windspeed <= 110:
    print(windspeed, "mph Is a Category 2 hurricane")
    
elif windspeed >= 111 and windspeed <= 130:
    print(windspeed, "mph Is a Category 3 hurricane")
    
elif windspeed >= 131 and windspeed <= 155:
    print(windspeed, "mph Is a Category 4 hurricane")
    
elif windspeed >= 156:
    print(windspeed, "mph and over is a Category 5 hurricane")
