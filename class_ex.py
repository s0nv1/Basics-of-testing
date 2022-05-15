
class Car:
    
    def __init__(self, name, model, year, color):
        self.name = name 
        self.model = model 
        self.year = year 
        self.color = color
        self.km = 0
    
    def repaint(self, color):
        self.color = color
    
    def kilometr(self):
        self.km += 100
    
