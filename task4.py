'''#Question 1

class Circle:
    def __init__(self,radii):
        self.radii = radii
        
radii_listing = Circle([10,501,22,37,100,999,87,351])
print(f"the list of radii are - {radii_listing.radii}")

#Question 2
class Circle:
    
    __pi = 3.141
    
    def __init__(self,radii):
        self.radii = radii
        
radii_listing = Circle([10,501,22,37,100,999,87,351])
print(f"the list of radii are - {radii_listing.radii}")

#Question 3
class circle :
    __p1 = 3.141
    
    def __init__(self , radii):
        self.radii = radii
        
    def parameter(self):
        return 2 * self.__p1 * self.radii 
        
    def area(self):
        return self.__p1 * self.radii **2

circle_parameter = circle(8)
print(circle_parameter.parameter())
circle_area = circle(8)
print(circle_area.area())

#Question 4
#partA
class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1  # Default channel
        self.volume = 50  # Default volume
        self.on = False   # TV is initially turned off

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50
        self.on = False

    def toggle_power(self):
        self.on = not self.on

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Example usage of TV class
if __name__ == "__main__":
    tv1 = TV("Panasonic")
    print(tv1.status())  # Output: Panasonic at channel 1, volume 50
    tv1.increase_volume()
    tv1.set_channel(8)
    print(tv1.status())  # Output: Panasonic at channel 8, volume 51
    tv1.reset_tv()
    print(tv1.status())  # Output: Panasonic at channel 1, volume 50'''

#part B
class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1  # Default channel
        self.volume = 50  # Default volume
        self.on = False   # TV is initially turned off

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50
        self.on = False

    def toggle_power(self):
        self.on = not self.on

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"{self.brand} LED TV - Screen Thickness: {self.screen_thickness} mm, " \
               f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan} years, " \
               f"Refresh Rate: {self.refresh_rate} Hz"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"{self.brand} Plasma TV - Screen Thickness: {self.screen_thickness} mm, " \
               f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan} years, " \
               f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: {self.viewing_angle}, " \
               f"Backlight: {self.backlight}"

# Example usage of LED TV and Plasma TV classes
if __name__ == "__main__":
    led_tv1 = LedTV("Sony", 10, "Low", 8, 120)
    print(led_tv1.status())  # Output: Sony at channel 1, volume 50
    print(led_tv1.display_details())
    
    plasma_tv1 = PlasmaTV("Samsung", 15, "Medium", 10, 100, "Wide", "Yes")
    print(plasma_tv1.status())  # Output: Samsung at channel 1, volume 50
    print(plasma_tv1.display_details())




    


    


