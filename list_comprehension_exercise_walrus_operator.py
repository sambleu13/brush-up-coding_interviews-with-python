# You need the temperature in both the expression and the conditional so this is a challenge. 
# The walrus operator (:=) solves this problem. It allows you to run an expression 
# while simultaneously assigning the output value to a variable. 

import random
def get_weather_data():
    return random.randrange(90, 110) # generate fake weather temperature

print([temp for _ in range(20) if (temp:= get_weather_data()) >= 100])
