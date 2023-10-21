from driver import Driver
from gp import GP
from timeform import TimeForm
from time_gp import Time


class Chempionship:
    def __init__(self) -> None:
        self.driver_list: list[Driver] = []
        self.gp_list: list[GP] = []
        self.end_time_list: list[Time] = []
        # return and_time_list.sort()
        # print(and_time_list)

    def helper_create_driver(self, gp_name, driver: Driver):
        for gp in self.gp_list:
            if gp.name == gp_name:
                gp.add_driver(driver)

    def create_driver(self, name, gp_name):
        driver = Driver(name)
        self.driver_list.append(driver)
        print('driver yaratildi')
        self.helper_create_driver(gp_name, driver)
        return driver
    
    def get_drivers(self):
        return self.driver_list
    
    def get_driver(self, driver_name):
        for driver in self.driver_list:
            if driver.name == driver_name:
                return driver
        return None

    def define_gp(self, name):
        gp = GP(name)
        self.gp_list.append(gp)
        return gp

    def get_gp(self, name):
        for gp in self.gp_list:
            if gp.name == name:
                return gp
        return None
    
    def set_time(self, gp: GP, driver: Driver, tugash_vaqti: TimeForm):
        time = Time(gp, driver, tugash_vaqti)
        self.end_time_list.append(time)
        return time
