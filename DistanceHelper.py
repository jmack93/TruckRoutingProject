# John R. McKahan II Student ID:
#This is used for getting the distance info loaded in

import csv
import CSVHelper

import Hashfile

#This dictionary will hold the address values and the delivery ID values that correspond with them
dictionaryaddresses = {}

#This dictionary will hold the delivery ID values, with the mileage values between them
dictionarymile = {}


#addresshashfile = Hashfile.Hashfile()

#This will populate the "dictionaryaddresses" dictionary with the delivery ID, the name of the location, and the address

with open('WGUAddresses.csv') as theaddressdata:
    addressreader = csv.reader(theaddressdata)
    for row in addressreader:
        dictionaryaddresses[row[0]] ={'deliverID': row[0], 'hubname': row[1], 'del_address': row[2]}

#This will populate the "Dictionarymile" dictionary with the Delivery ID, and the mileage values between them
with open('WGUMiles.csv') as themilesdata:
    milereader = csv.reader(themilesdata)
    for row in milereader:
        dictionarymile[row[0]] = {'deliveryID': row[0], '0': row[1], '1': row[2], '2': row[3], '3': row[4], '4': row[5], '5': row[6], '6': row[7],
                                    '7': row[8], '8':row[9], '9':row[10], '10':row[11], '11':row[12], '12':row[13], '13':row[14],
                                   '14':row[15], '15':row[16], '16':row[17], '17':row[18],'18':row[19], '19':row[20], '20':row[21],
                                    '21':row[22], '22':row[23], '23':row[24], '24':row[25], '25':row[26], '26':row[27]}





#Big O Complexity O(n)
#This will return the delivery ID, by looking up the address from the dictionaryaddress dictionary
def get_deliverID(address):

    for row in dictionaryaddresses:
        if dictionaryaddresses[row]['del_address'] == address:
            testid = dictionaryaddresses[row]['deliverID']
            return testid
    else:
            return "Error obtaining delivery ID"


#Big O Complexity O(1)
#Calculates the mileage between two addresses
def get_mileage(address1, address2):
    mileage = dictionarymile[address1][address2]

    return mileage



#Big O Complexity O(n)
def get_deliverIDnow(listofpackageid):

    deliveryroutelist = []
    for x in listofpackageid:
        locationadd = CSVHelper.fullpackagelist.get_value(x).get_address()
#
        thedeliveryid = get_deliverID(locationadd)

        deliveryroutelist.append(thedeliveryid)

    return deliveryroutelist



#Big O complexity O(n^2)

#This algorithm takes a "greedy" approach to solving the problem of finding the shortest distance to deliver the packages
#By taking a "greedy" approach, this algorithm will always search for the next shortest location to visit next. If two locations are both the shortest, one is chosen at random.
#All solutions provided by this algorithm meet the requirements of this project.
def greedyroute(truckpackages):


  #The hub variable is set to zero to represent the hub/starting location's ID
    hub = 0
  #The "bestroute" list is what hold the values that will compose the best route as determined by the algorithm.
    bestroute = []

  #the "LowestID" will hold the LocationID to be added to the "bestroute" the value of 100 is just a placeholder I picked at random.
    lowestid = 100



    while len(truckpackages) != 0:
        #"Thelowestchoice" will hold the first variable, the miles between the hub, and the first location in the route
        #In order for this to work the first time, "Thelowestchoice" must be lower than any possible mileage.
        #This should always be the case, and in terms of scalability, this distance is larger than the diameter of the Earth in miles
        #Additionally, this variable can always be updated if the time comes where the needs of the business are greater and demand more mileage.
        thelowestchoice = 8000.9
        for locationid in truckpackages:
            #This prevents the lowest mileage from being 0, as the hub will be updated
            if locationid != hub:

                #This calculates the mileage between the hub location, and the starting location
                milesbetween = float(get_mileage(str(hub), str(locationid)))


                if milesbetween < thelowestchoice:
                    thelowestchoice = milesbetween
                    lowestid = locationid

        if locationid not in bestroute:
            #The new "Hub" becomes the location that the truck visited, so that new comparisons can be made to determine the next lowest route to take
            hub = lowestid
            #Removes the package from the list of truck packages as to not visit a redundant location
            truckpackages.remove(lowestid)
            #Adds the "best" choice to the bestroute list which will be used by the truck
            bestroute.append(lowestid)

    return bestroute
