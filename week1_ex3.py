class Thermostat:
    min_temp=15
    max_temp=30
    device_count=0
def __init__(self,location,initial_temp):
    self.location=location
    # reading=[]
    if initial_temp >= Thermostat.min_temp and \
        initial_temp <= Thermostat.max_temp:
        self.current_temp=initial_temp
        self.current_temp= initial_temp
    else:
        self.current_temp=Thermostat.min_temp
        self.readings=[self.current_temp]
def set_temperature(self,new_temp):
    if new_temp>=Thermostat.min_temp and new_temp <= Thermostat.max_temp:
        self.current_temp=new_temp
    else:
        print("Invalid Temp")
def get_average_temp(self):
    a=len(self.readings)
    if a == 0:
        return 0
    average =sum(self.readings)/a
    return average
def display_status(self):
    print(f"Location : {self.location}, temp : {self.current_temp}")
