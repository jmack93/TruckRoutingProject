# John R. McKahan II Student ID:

class Truck:

#This class is used to create trucks, which will be loaded and sent out to deliver the packages.
    def __init__(self, trucknumber):
        self.mileagetotal = 0
        self.trucknumber = trucknumber
        self.storage = []
        self.routinglocations = []
        self.milestolocal = []

#Big O Complexity O(1)
    def add_package(self, inventorypackage):
        self.storage = inventorypackage

    # Big O Complexity O(1)
    def add_miles(self, miles):
        self.milestolocal = miles

    # Big O Complexity O(1)
    def get_miles(self):
        return self.milestolocal

    # Big O Complexity O(1)
    def show_packages(self):
        return self.storage

    # Big O Complexity O(1)
    def remove_package(self, inventorypackage):
        invlist = self.storage
        invlist.remove(inventorypackage)

    # Big O Complexity O(1)
    def remove_route(self, routeloc):
        routelist = self.routinglocations
        routelist.remove(routeloc)

    # Big O Complexity O(1)
    def add_route(self, routingloc):
        self.routinglocations = routingloc

    # Big O Complexity O(1)
    def show_route(self):
        return self.routinglocations


