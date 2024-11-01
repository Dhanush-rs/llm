from typing import Type, List
from entities.vechicles import Vehicle
class Driver:
    
    def __init__(self, name, gender, age, vehicle_name, vehicle_number, current_location = (0,0)) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.earnings = 0
        self.is_available = True
        self.current_location = current_location
        self.vechicle = Vehicle(vehicle_name, vehicle_number)
    
    def update_earning(self, amount):
        self.earnings += amount
        
    def get_is_available(self):
        return self.is_available
    
    def set_is_available(self, available):
        self.is_available = available
        
    def get_location(self):
        return self.current_location
    
    def set_location(self, location):
        self.current_location = location
    
    
    