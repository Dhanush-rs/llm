
class User:
    
    def __init__(self, name, gender, age, current_location=(0,0)) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.current_location = current_location
        
    def set_location(self, location):
        self.current_location = location
        
    def get_location(self):
        return self.current_location
    
        
    