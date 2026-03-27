from abc import ABC, abstractmethod
class DeliveryVehicle(ABC):
    def __init__(self,vehicle_id):
        self.vehicle_id=vehicle_id
    @abstractmethod
    def estimated_time(self,distance):
        pass

    def desribe(self):
        return f"{self.__class__.__name__} {self.vehicle_id}"
    
class Drone(DeliveryVehicle): 
    def estimated_time(self, distance):
        return distance/50.0
    
class CargoVan(DeliveryVehicle):
    def __init__(self, vehicle_id,loading_time):
        super().__init__(vehicle_id)
        self.loading_time=loading_time

    def estimated_time(self, distance):
        return (distance/80.0)+self.loading_time
    
class CourierService:
    def __init__(self,name):
        self.name=name
        self.fleet=[]

    def add_vehicle(self,vehicle):
        self.fleet.append(vehicle)
    def get_fastest(self,distance):
        lowest_time=float('inf')
        vehicle_with_lowest_time= None
        for vehicle in self.fleet:
            current_time=vehicle.estimated_time(distance)
            if current_time<lowest_time:
                lowest_time=current_time
                vehicle_with_lowest_time=vehicle
        print (f"Dispatching {vehicle_with_lowest_time} - ETA : {}")
