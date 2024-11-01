import math
from entities.users import User
from entities.drivers import Driver

class RideService:
    
    def __init__(self) -> None:
        self.users = {}
        self.drivers = {}
        self.user_rides = {}
    
    def add_user(self, user_data):
        user_name, gender, age = user_data.split(",")
        user = User(user_name, gender, age)
        self.users[user_name] = user
        
    def update_user_location(self, name, location):
        user = self.users.get(name)
        user.set_location(location)
    
    def add_driver(self, driver_details, vehicle_details, current_location):
        # driver_details, vehicle_details, current_location = driver_data.split(",")
        name, gender, age = driver_details.split(",")
        vehicle_name, number = vehicle_details.split(",")
        
        driver = Driver(name, gender, age, vehicle_name, number, current_location)
        self.drivers[name]=driver
    
    def find_distance(self, source, destination):
        result = (abs(destination[1]-source[1])**2+ abs(destination[0]-source[0])**2)
        return math.sqrt(result)
    
    def check_if_nearby(self, driver, source):
        driver_location = driver.get_location()
        # print(source, driver_location)
        distance = self.find_distance(source, driver_location)
        # print(distance)
        if distance<=5:
            return True
        return False
                             
    def find_ride(self, username, source, destination):
        nearby_drivers = []
        for _,driver in self.drivers.items():
            if driver.is_available:
                is_nearby = self.check_if_nearby(driver, source)
                if is_nearby:
                    nearby_drivers.append(driver.name)
        if nearby_drivers:
            print(f"{nearby_drivers} [Available]")
            if not username in self.user_rides:
                self.user_rides[username] = {}
            self.user_rides[username]["destination"]= destination
        else:
            print("No ride found [Since all the driver are more than 5 units away from user]")
        
    
    def choose_ride(self, username, driver):
        try:
            driver = self.drivers.get(driver)
            self.user_rides[username]["driver"] = driver
            print("ride started")
        except KeyError as e:
            print(f"{username} is not in the nearby vicinity check by calling find_ride() method")
        
    def calculate_bill(self, username):
        user = self.users[username]
        driver = self.user_rides[username]["driver"]
        destination = self.user_rides[username]["destination"]
        travelled_distance = self.find_distance(destination, user.get_location())
        amount = round(travelled_distance)
        print("ride Ended bill amount $", amount)
        user.set_location(destination)
        driver.set_location(destination)
        driver.update_earning(amount)
        
        
    def find_total_earning(self):
        for _,driver in self.drivers.items():
            print(f"{driver.name} earns {driver.earnings}")
            
    def change_driver_status(self, name, status):
        driver = self.drivers.get(name)
        driver.set_is_available==status
    
    
    