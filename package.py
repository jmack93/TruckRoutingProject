# John R. McKahan II Student ID:
class Package(object):


#This class is used to contain the package information which will be stored in a hashtable, as an object.
    packageid = 0
    deliveryaddress = ""
    deliverycity = ""
    deliveryzipcode = 0
    deliverydeadline = ""
    packageweight = 0
    deliverynotes = ""
    deliverystatus = ""

    def __init__(self, packageid, deliveryaddress, deliverycity, deliverystate, deliveryzipcode,
                 deliverydeadline,  packageweight, deliverynotes, deliverystatus):
        self.id = packageid
        self.address = deliveryaddress
        self.city = deliverycity
        self.state = deliverystate
        self.zipcode = deliveryzipcode
        self.deadline = deliverydeadline
        self.weight = packageweight
        self.notes = deliverynotes
        self.status = deliverystatus

    def gen_package(packageid, deliveryaddress, deliverycity, deliverystate, deliveryzipcode, deliverydeadline,
                    packageweight, deliverynotes, deliverystatus):

        package = Package(packageid, deliveryaddress, deliverycity, deliverystate, deliveryzipcode,
                          deliverydeadline, packageweight, deliverynotes, deliverystatus)
        package.id = packageid
        package.deliveryaddress = deliveryaddress
        package.deliverycity = deliverycity
        package.deliverystate = deliverystate
        package.deliveryzipcode = deliveryzipcode
        package.deliverydeadline = deliverydeadline
        package.packageweight = packageweight
        package.deliverynotes = deliverynotes
        package.deliverystatus = deliverystatus

        return package

    # Big O Complexity O(1)
    def set_id(self, z):
        self.id = z

    # Big O Complexity O(1)
    def get_id(self):
        return self.id

    # Big O Complexity O(1)
    def set_address(self, z):
        self.address = z

    # Big O Complexity O(1)
    def get_address(self):
        return self.address

    # Big O Complexity O(1)
    def get_city(self):
        return self.city

    # Big O Complexity O(1)
    def set_city(self, z):
        self.city = z

    # Big O Complexity O(1)
    def set_state(self, z):
        self.state = z

    # Big O Complexity O(1)
    def get_state(self):
        return self.state

    # Big O Complexity O(1)
    def set_zip(self, z):
        self.zipcode = z

    # Big O Complexity O(1)
    def get_zip(self):
        return self.zipcode

    # Big O Complexity O(1)
    def set_deadline(self, z):
        self.deadline = z

    # Big O Complexity O(1)
    def get_deadline(self):
        return self.deadline

    # Big O Complexity O(1)
    def set_weight(self, z):
        self.weight = z

    # Big O Complexity O(1)
    def get_weight(self):
        return self.weight

    # Big O Complexity O(1)
    def set_notes(self, z):
        self.notes = z

    # Big O Complexity O(1)
    def get_notes(self):
        return self.notes

    # Big O Complexity O(1)
    def set_status(self, z):
        self.status = z

    # Big O Complexity O(1)
    def get_status(self):
        return self.status

    # Big O Complexity O(1)
    def __str__(self):
        return self.id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes, self.status
