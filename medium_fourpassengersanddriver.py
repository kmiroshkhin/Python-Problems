'''A typical car can hold 4 passengers and 1 driver, overall allowing 5 people to travel around.
Given n number of people, return how many cars are needed to seat everyone comfortably.
'''

def cars_needed(n):
    return round((n/5)+0.4999,0)

print(cars_needed(5))