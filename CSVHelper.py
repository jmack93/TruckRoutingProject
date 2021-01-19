# John R. McKahan II Student ID:
import csv
import package

import Hashfile


#This holds all of the package information, searchable by the packageID(Key), and containing a package object with information inside(Value)
fullpackagelist = Hashfile.Hashfile()

#This contains the package address(Value), searchable by the packageID (Key)
packageaddresshash = Hashfile.Hashfile()

with open('packagefile.csv') as packagedata:

    reader = csv.reader(packagedata)
    count = 0

    for row in reader:


        packageid = row[0]
        deliveryaddress = row[1]
        deliverycity = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]
        status = "At the hub"

        newpackage = package.Package(packageid, deliveryaddress, deliverycity, state, zip,
                                     deadline, weight, notes, status)
        infovalue = newpackage.__str__()

        maybevalue = [packageid, deliveryaddress, deliverycity, state, zip, deadline, weight, notes, status]
        newpackageid = int(packageid)

        fullpackagelist.add_value(newpackageid, newpackage)
        packageaddresshash.add_value(newpackageid, maybevalue[1])

        #As there are only 40 packages, this will break the loop once all of the packages have been added.
        if count >= 40:


            break

        count += 1
#Big O Time Complexity O(1)

def FixTypo():
    fullpackagelist.get_value(26).set_address("5383 S 900 East #104")
    fullpackagelist.get_value(25).set_address("5383 S 900 East #104")


#Big O Time Complexity O(1)

def FixWrongAddress():
    fullpackagelist.get_value(9).set_address("410 S State St")
    fullpackagelist.get_value(9).set_notes("Corrected Address!")
    fullpackagelist.get_value(9).set_zip("84111")

#Big O Time Complexity O(1)
def printthetable():
    for x in range(1,41):
        print(fullpackagelist.get_value(x).__str__())



#Big O Time Complexity O(1)
def resetthevalues():
    for x in range(1,41):
        fullpackagelist.get_value(x).set_status("At the Hub")

#Big O Time Complexity O(1)
def resetWrongAddress():
    fullpackagelist.get_value(9).set_address("300 State St")
    fullpackagelist.get_value(9).set_notes("Wrong address")
    fullpackagelist.get_value(9).set_zip("84103")

FixTypo()
