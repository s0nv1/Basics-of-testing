
def function(n, start=0):
    if start == len(n) - 1:
        return n[start]
    else:
        return n[start] + function(n, start+1)
        
def wrapper(n, ind=0):
    if ind == len(n) - 1:
        return n[ind] ** 2
    else:
        return n[ind] ** 2 + wrapper(n, ind + 1)


class Bus:
    def __init__(self, name, age, km, color):
        self.name = name 
        self.age = age 
        self.km = km
        self.color = color
    
    def set_color(self, color):
        self.color = color

    def set_km(self, km):
        self.km = km
    
    def set_age(self):
        self.age += 1


    
