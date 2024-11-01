from services.ride_service import RideService 
def main():
    ride_service = RideService()
    # Register passengers and update lodation
    ride_service.add_user("Abhishek, M, 23")
    ride_service.update_user_location("Abhishek",(0,0)) 
    
    ride_service.add_user("Rahul, M, 29")
    ride_service.update_user_location("Rahul",(10,0))
    
    ride_service.add_user("Nandini, F, 22") 
    ride_service.update_user_location("Nandini",(15,6))
    
    # Register drivers and update location
    ride_service.add_driver("Driver1, M, 22","Swift, KA-01-12345",(10,1))
    ride_service.add_driver("Driver2, M, 29","Swift, KA-01-12345",(11,10))
    ride_service.add_driver("Driver3, M, 24","Swift, KA-01-12345",(5,3))

    # find and execute rides
    ride_service.find_ride("Abhishek",(0,0),(20,1))
    ride_service.find_ride("Rahul" ,(10,0),(15,3))
    ride_service.choose_ride("Rahul","Driver1")
    
    ride_service.calculate_bill("Rahul")
    
    ride_service.find_ride("Nandini",(15,6),(20,4))
    
    ride_service.change_driver_status("Driver1", False)
    print(ride_service.drivers.get("Driver1").get_is_available())
    # total earnings
    ride_service.find_total_earning()

if __name__ == "__main__":
    main()