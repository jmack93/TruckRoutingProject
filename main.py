# John R. McKahan II Student ID:
import DistanceHelper
import CSVHelper
import datetime
import Truck



#Big O complexity O(1)
#This function takes the route of the truck object input and calculates the total mileage
def calculatetotalmileageoftruckroute(truckinput):
    hub = 0
    totalroutelength = 0
    iteratethatlist = 0
    routetotake = truckinput.show_route()

    for location in routetotake:
            milestogetthere = float(DistanceHelper.get_mileage(str(hub), location))
            totalroutelength += milestogetthere

            hub = location
            iteratethatlist += 1

    return totalroutelength


#Big O complexity O(1)
#This function gets the mileages between distances in the routelist of the truck, starting at the hub, to index 0.
def get_distances(truck):

    firstdistance = truck.show_route().__getitem__(0)
    thehub = 0
    distancelist = []
    distancebetweenfirst = DistanceHelper.get_mileage(str(thehub),firstdistance)
    distancelist.append(float(distancebetweenfirst))



    for routenumber in range(1, len(truck.show_route())):
        hublocation = truck.show_route().__getitem__(routenumber - 1)
        nextdestination = truck.show_route().__getitem__(routenumber)
        mileage = DistanceHelper.get_mileage(str(hublocation), str(nextdestination))

        mileageint = float(mileage)


        distancelist.append(mileageint)


    return distancelist


#Big O complexity O(1)
#This calculates the total mileage of the truck, based upon the index.
#This adds the index with the ones before it
def mileagecalculator(truck, index):

    totalmiles = 0.00
    for x in range(0, index+1):

       totalmiles += float(truck.get_miles().__getitem__(x))

    return totalmiles


#Big O complexity O(n^3)
def simulations(truck, time):
    #Trucks are allowed to leave the station at 08:00AM, this value corresponds to that time, in seconds.
    startofday = datetime.timedelta(seconds=28800)
    #Truck three will leave the hub at 10:20 AM, this value corresponds to that time, in seconds.
    startoftruckthree = datetime.timedelta(seconds=37200)


    totalmiles = 0

    totaltimetolocation = 0

    packageidlist = []
    returnstart = 0
    gatekeeper = 0
    tester = 1
    distancefloat = 0
    firstmiles = 0


    #This loops through the packageids within the truck and sets their status to "On the Truck"
    for packageid in truck.show_packages():
        if str(packageid) == str(CSVHelper.fullpackagelist.get_value(packageid).get_id()):
            CSVHelper.fullpackagelist.get_value(packageid).set_status("On The Truck")
    #This loops through the data of miles/routelength of the Truck
    for mileagedata in range (len(truck.get_miles())):

        #This is the mileage to the indexed location
        mileageint = float(truck.get_miles().__getitem__(mileagedata))

        #This calculates how much time has elapsed by taking the inputted time, and subtracting the 08:00AM start time from it
        timeelapsed = (time - startofday)

        #This returns the value of "timeelapsed" in seconds
        secondstotal = timeelapsed.total_seconds()

        #The miles traveled is equal to 0.005 times the number of seconds, as for every second that passes, 0.005 miles have been traveled
        #(18miles per hour, divided by 60 minutes per hour, divided by 60 seconds per minute)
        milestraveled = (0.005 * secondstotal)

        milestogettolocation = mileageint
        totalmiles += milestogettolocation
        #Time to get to location is equivalent to 200 times the amount of miles, in seconds. It takes 200 seconds to travel 1 mile at 18mph.
        timetoggettolocation = (200) * mileageint
        totaltimetolocation += timetoggettolocation



        if milestraveled > mileagecalculator(truck, mileagedata):
                #This obtains the delivery location from the truck route
                deliveryid = (truck.show_route().__getitem__(mileagedata))

                #this is used to add with the start of the day to return the total timestamp to add, to verify
                # that packages have been delivered at the correct time
                supertime = datetime.timedelta(seconds= totaltimetolocation)
                timestamptoadd =(supertime + startofday)

                for packageid in truck.show_packages():
                    if str(deliveryid) == str(DistanceHelper.get_deliverID(CSVHelper.fullpackagelist.get_value(packageid).get_address())):


                        CSVHelper.fullpackagelist.get_value(packageid).set_status("Delivered! by Truck 2 " + str(timestamptoadd))



                        packageidlist.append(packageid)
                        returnstart = timestamptoadd


        #This is used later on in calculating the total miles of the routes traveled
        firstmiles += mileagecalculator(truck, mileagedata)

        #Returnstamptoadd is iniated with 20,000,000 seconds, once the first delivery is made by truck 2
        #The returnstart value will be lower, and make the next "if" possible to enter.
        returnstamptoadd = datetime.timedelta(seconds= 20000000)

        if int(len(packageidlist)) == int(len(truck.show_packages())):
            if time >= returnstart:



                distancetohub = DistanceHelper.get_mileage(str(truck.show_route().__getitem__(-1)),str(0))

                returntimeelapsed = (time - returnstart)
                distancefloat = float(distancetohub)
                returnsecondstotal = returntimeelapsed.total_seconds()

                returnmilestraveled = (0.005 * returnsecondstotal)


                returntimetoggettolocation = (200) * distancefloat

                if returnmilestraveled >= distancefloat:
                    timetoreturn = returntimetoggettolocation

                    timestampreturnadd = datetime.timedelta(seconds= timetoreturn)
                    returnstamptoadd = (returnstart + timestampreturnadd)


    #If the time is greater, then the truck(2) is back at the station
    if time >= returnstamptoadd:
            #Tester is equivalent to 0, but is originally equivalent to 1. If this if statement is not true, then the next section will not proceed
            tester = 0
    startofthree = returnstamptoadd

    threetotalmiles = 0
    threetimetoggettolocation = 0
    threetotaltimetolocation = 0
    emptytruck = []
    threepackageidlist = []
    threereturnstart = 0

    #Gatekeeper is equivalent to zero
    gatekeeper = tester

    if gatekeeper == 0 and time >= startoftruckthree:
#This fixes the wrong address at 10:20AM in order to provide an accurate route and delivery location for package ID 9
#Important note, Truck 3 is solely a placeholder name for Truck2, reloaded, as certain packages must be delivered on Truck2.
#As Truck2 has returned to the station, "Truck 3" is simply truck 2, reloaded.
        CSVHelper.FixWrongAddress()
        testtruck3 = set(DistanceHelper.get_deliverIDnow(optimizedpackagesfor3))
        testroutelisttruck3 = DistanceHelper.greedyroute(testtruck3)
        Truck3.add_route(testroutelisttruck3)
        Truck3.add_miles(get_distances(Truck3))
        for packageid in Truck3.show_packages():

            if str(packageid) == str(CSVHelper.fullpackagelist.get_value(packageid).get_id()):
                CSVHelper.fullpackagelist.get_value(packageid).set_status("On The Truck")
        for truckmileagedata in range(len(Truck3.get_miles())):


            threemileageint = float(Truck3.get_miles().__getitem__(truckmileagedata))

            threetimeelapsed = (time - startoftruckthree)

            threesecondstotal = threetimeelapsed.total_seconds()

            threemilestraveled = (0.005 * threesecondstotal)

            threemilestogettolocation = threemileageint
            threetotalmiles += threemilestogettolocation
            threetimetoggettolocation = (200) * threemileageint
            threetotaltimetolocation += threetimetoggettolocation

            if threemilestraveled >= mileagecalculator(Truck3, truckmileagedata):

                threedeliveryid = (Truck3.show_route().__getitem__(truckmileagedata))
                threesupertime = datetime.timedelta(seconds=threetotaltimetolocation)

                threetimestamptoadd = (threesupertime + startoftruckthree)

                for packageid in Truck3.show_packages():
                     if str(threedeliveryid) == str(DistanceHelper.get_deliverID(CSVHelper.fullpackagelist.get_value(packageid).get_address())):


                        CSVHelper.fullpackagelist.get_value(packageid).set_status("Delivered! by Truck 2, reloaded!" + str(threetimestamptoadd))



                        threepackageidlist.append(packageid)

    #This calculates and returns the total mileage
    totalmileage = float(distancetohub) + float(calculatetotalmileageoftruckroute(Truck2) + float(calculatetotalmileageoftruckroute(Truck3)))
    return totalmilelist.append(totalmileage)





#This functions similarly to "Simulations" but starts the day at 9:05AM
def delayedsimulation(time):
    #Truck 1 will be leaving the station at 09:05AM, the seconds within the startofdaydelayed correspond to this time.
    startofdaydelayed = datetime.timedelta(seconds=32700)

    totalmiles = 0

    totaltimetolocation = 0

    for packageid in Truck1.show_packages():
        if str(packageid) == str(CSVHelper.fullpackagelist.get_value(packageid).get_id()):
            CSVHelper.fullpackagelist.get_value(packageid).set_status("On The Truck")
    for mileagedata in range (len(Truck1.get_miles())):

        mileageint = float(Truck1.get_miles().__getitem__(mileagedata))

        timeelapsed = (time - startofdaydelayed)

        secondstotal = timeelapsed.total_seconds()

        milestraveled = (0.005 * secondstotal)

        milestogettolocation = mileageint
        totalmiles += milestogettolocation
        timetoggettolocation = (200) * mileageint
        totaltimetolocation += timetoggettolocation



        if milestraveled >= mileagecalculator(Truck1, mileagedata):

                deliveryid = (Truck1.show_route().__getitem__(mileagedata))
                supertime = datetime.timedelta(seconds= totaltimetolocation)
                timestamptoadd =(supertime + startofdaydelayed)

                for packageid in Truck1.show_packages():
                    if str(deliveryid) == str(DistanceHelper.get_deliverID(CSVHelper.fullpackagelist.get_value(packageid).get_address())):


                        CSVHelper.fullpackagelist.get_value(packageid).set_status("Delivered! by Truck 1 " + str(timestamptoadd))



    return totalmilelist.append(calculatetotalmileageoftruckroute(Truck1))





#This functions similarly to the previous functions, but does not return the mileage, as it is not required for the packageID lookups at the given times.
def simulationsforuser(truck, time):
    #Trucks are allowed to leave the station at 08:00AM, this value corresponds to that time, in seconds.
    startofday = datetime.timedelta(seconds=28800)
    #Truck three will leave the hub at 10:20 AM, this value corresponds to that time, in seconds.
    startoftruckthree = datetime.timedelta(seconds=37200)


    totalmiles = 0

    totaltimetolocation = 0

    packageidlist = []
    returnstart = 0
    gatekeeper = 0
    tester = 1
    distancefloat = 0
    firstmiles = 0


    #This loops through the packageids within the truck and sets their status to "On the Truck"
    for packageid in truck.show_packages():
        if str(packageid) == str(CSVHelper.fullpackagelist.get_value(packageid).get_id()):
            CSVHelper.fullpackagelist.get_value(packageid).set_status("On The Truck")
    #This loops through the data of miles/routelength of the Truck
    for mileagedata in range (len(truck.get_miles())):

        #This is the mileage to the indexed location
        mileageint = float(truck.get_miles().__getitem__(mileagedata))

        #This calculates how much time has elapsed by taking the inputted time, and subtracting the 08:00AM start time from it
        timeelapsed = (time - startofday)


        secondstotal = timeelapsed.total_seconds()

        milestraveled = (0.005 * secondstotal)

        milestogettolocation = mileageint
        totalmiles += milestogettolocation
        timetoggettolocation = (200) * mileageint
        totaltimetolocation += timetoggettolocation



        if milestraveled > mileagecalculator(truck, mileagedata):

                deliveryid = (truck.show_route().__getitem__(mileagedata))

                supertime = datetime.timedelta(seconds= totaltimetolocation)
                timestamptoadd =(supertime + startofday)

                for packageid in truck.show_packages():
                    if str(deliveryid) == str(DistanceHelper.get_deliverID(CSVHelper.fullpackagelist.get_value(packageid).get_address())):




                        timetoadd = datetime.timedelta(seconds= totaltimetolocation)


                        CSVHelper.fullpackagelist.get_value(packageid).set_status("Delivered! by Truck 2 " + str(timestamptoadd))


                        packagetoberemoved = packageid
                        packageidlist.append(packageid)
                        returnstart = timestamptoadd



        returnstamptoadd = datetime.timedelta(seconds= 20000000)

        if int(len(packageidlist)) == int(len(truck.show_packages())):
            if time >= returnstart:



                distancetohub = DistanceHelper.get_mileage(str(truck.show_route().__getitem__(-1)),str(0))

                returntimeelapsed = (time - returnstart)
                distancefloat = float(distancetohub)
                returnsecondstotal = returntimeelapsed.total_seconds()

                returnmilestraveled = (0.005 * returnsecondstotal)

                returnmilestogettolocation = distancetohub
                returntimetoggettolocation = (200) * distancefloat

                if returnmilestraveled >= distancefloat:
                    timetoreturn = returntimetoggettolocation

                    timestampreturnadd = datetime.timedelta(seconds= timetoreturn)
                    returnstamptoadd = (returnstart + timestampreturnadd)



    if time >= returnstamptoadd:

            tester = 0
    startofthree = returnstamptoadd

    threetotalmiles = 0
    threetimetoggettolocation = 0
    threetotaltimetolocation = 0
    emptytruck = []
    threepackageidlist = []
    threereturnstart = 0

    gatekeeper = tester

    if gatekeeper == 0 and time >= startoftruckthree:
#This fixes the wrong address at 10:20AM in order to provide an accurate route and delivery location for package ID 9
        CSVHelper.FixWrongAddress()
        testtruck3 = set(DistanceHelper.get_deliverIDnow(optimizedpackagesfor3))
        testroutelisttruck3 = DistanceHelper.greedyroute(testtruck3)
        Truck3.add_route(testroutelisttruck3)
        Truck3.add_miles(get_distances(Truck3))
        for packageid in Truck3.show_packages():

            if str(packageid) == str(CSVHelper.fullpackagelist.get_value(packageid).get_id()):
                CSVHelper.fullpackagelist.get_value(packageid).set_status("On The Truck")
        for truckmileagedata in range(len(Truck3.get_miles())):


            threemileageint = float(Truck3.get_miles().__getitem__(truckmileagedata))

            threetimeelapsed = (time - startoftruckthree)

            threesecondstotal = threetimeelapsed.total_seconds()

            threemilestraveled = (0.005 * threesecondstotal)

            threemilestogettolocation = threemileageint
            threetotalmiles += threemilestogettolocation
            threetimetoggettolocation = (200) * threemileageint
            threetotaltimetolocation += threetimetoggettolocation

            if threemilestraveled >= mileagecalculator(Truck3, truckmileagedata):

                threedeliveryid = (Truck3.show_route().__getitem__(truckmileagedata))
                threesupertime = datetime.timedelta(seconds=threetotaltimetolocation)

                threetimestamptoadd = (threesupertime + startoftruckthree)
                # print(threesupertime)
                for packageid in Truck3.show_packages():
                     if str(threedeliveryid) == str(DistanceHelper.get_deliverID(CSVHelper.fullpackagelist.get_value(packageid).get_address())):
                        threetimetoadd = datetime.timedelta(seconds=threetotaltimetolocation)

                        CSVHelper.fullpackagelist.get_value(packageid).set_status("Delivered! by Truck 2, reloaded!" + str(threetimestamptoadd))


                        threepackagetoberemoved = packageid
                        threepackageidlist.append(packageid)
                        threereturnstart = threetimestamptoadd




#This function is used to simulate the entire day. This function contains two functions within it, which are explained
#In further detail above.
def simulatetheentireday(truck,time):
    i = 0
    simulations(truck, time)

    if time >= datetime.timedelta(seconds= 32700):
        delayedsimulation(time)

    totalmilestraveled = totalmilelist[0] + totalmilelist[1]
    print("Total miles traveled is : " + str(totalmilestraveled))




#This function is used to allow the user to input an hour and minute, and run the simulation based upon that time input.
#This function contains two functions which are explained in further detail above.
def simulatetheentiredaygiventime(truck,hour,minute):
    i = 0
    inthour = int(hour)
    intminute = int(minute)
    thetimeinseconds = datetime.timedelta(hours = inthour)
    thetimeinminutes = datetime.timedelta(minutes = intminute)
    printland = (thetimeinminutes + thetimeinseconds)
    time = datetime.timedelta(seconds= printland.seconds)
    simulationsforuser(truck, time)

    if time >= datetime.timedelta(seconds= 32700):
        delayedsimulation(time)





testnine = datetime.timedelta(seconds=29800)


if __name__ == '__main__':
    #This initiates the truck objects, an important note is that for this project, Truck1, and Truck2 represent their respective trucks, but,
    #Truck3 is functioning as a reloaded Truck2.

    Truck1 = Truck.Truck(1)
    Truck2 = Truck.Truck(2)
    Truck3 = Truck.Truck(3)

    #This list is used to hold mileage data from both the initial and delayed simulations. The contents of the list are added together
    #Which is then used to provide the user with a total mileage of the route
    totalmilelist = []

    #testtime is simply a placeholder for time to be used to simulate the entire day's package delivery. This corresponds to 25 hours, although
    #The package delivery is completed in full, shortly after 12:00PM.
    testtime = datetime.timedelta(seconds=90000)

    #The optimized packages for truck one, two, and three. An important note, as mentioned previously, truck3 is used after truck2 has already returned to the hub in the simulation
    #In this case, truck 3 is nothing more than a renamed truck2.
    #Packages were "optimized" by deciding which, based upon their delivery requirements, were of most importance for immediate delivery.

    optimizedpackagesfor2 = [34, 14, 15, 16, 39, 13, 37, 30, 20, 19, 29, 1, 3, 21, 40, 31]
    optimizedpackagesfor1 = [2, 6, 12, 22, 24, 25, 26, 27, 35]
    optimizedpackagesfor3 = [4, 5, 7, 8, 9, 10, 11, 17, 18, 23, 28, 32, 33, 36, 38]


    #The following, are sets of delivery IDs, without repetition, for the trucks delivery route. These call a function defined within
    #The "DistanceHelper" file, and obtains the delivery ID. From there, "DistanceHelper" has a function to determine
    #A good route for the list. This function contains a "Greedy" algorithm which is explained in more detail within the
    #"DistanceHelper" file
    testtruck2 = set(DistanceHelper.get_deliverIDnow(optimizedpackagesfor2))
    testtruck1 = set(DistanceHelper.get_deliverIDnow(optimizedpackagesfor1))

    testroutelisttruck2 = DistanceHelper.greedyroute(testtruck2)
    Truck2.add_route(testroutelisttruck2)

    testroutelisttruck1 = DistanceHelper.greedyroute(testtruck1)

    #This loads the Truck objects with information for their routing, packages, and mileage between destinations.
    Truck1.add_route(testroutelisttruck1)
    Truck1.add_package(optimizedpackagesfor1)

    Truck2.add_package(optimizedpackagesfor2)
    Truck3.add_package(optimizedpackagesfor3)

    Truck1.add_miles(get_distances(Truck1))
    Truck2.add_miles(get_distances(Truck2))

    print("--------------------------------------")
    print('Welcome to the WGUPS Routing Solution')
    print("--------------------------------------")
    print("To see a list of all of the packages with their delivery times, and simulate the day, please input 1 when prompted ")
    print("--------------------------------------")
    userinput = input("Please input a number")
    intuserinput = int(userinput)
    if intuserinput == 1:

        simulatetheentireday(Truck2,testtime)
        CSVHelper.printthetable()
        print("--------------------------------------")
        print("To display package information at a given time, please input 1")
        print("--------------------------------------")
        displaystatus = input("Input: ")
        if displaystatus == 1: print("Please select an hour to display, input an integer 08 - 24")
        hourinput = input("Select Hour, 08 - 24: ")
        print("--------------------------------------")
        print("Please select the minute to display, input an integer 0 - 59")
        minuteinput = input("Select Minute: ")

        CSVHelper.resetthevalues()
        CSVHelper.resetWrongAddress()
        simulatetheentiredaygiventime(Truck2,hourinput,minuteinput)
        CSVHelper.printthetable()
        print("--------------------------------------")
        print("--------------------------------------")
        print("To display package information at a given time, please input 1")
        print("--------------------------------------")
        twodisplaystatus = input("Input: ")
        if twodisplaystatus == 1: print("Please select an hour to display, input an integer 08 - 24")
        twohourinput = input("Select Hour, 08 - 24: ")
        print("--------------------------------------")
        print("Please select the minute to display, input an integer 0 - 59")
        twominuteinput = input("Select Minute: ")
        CSVHelper.resetthevalues()
        CSVHelper.resetWrongAddress()
        simulatetheentiredaygiventime(Truck2, twohourinput, twominuteinput)
        CSVHelper.printthetable()

        print("--------------------------------------")
        print("--------------------------------------")
        print("To display package information at a given time, please input 1")
        print("--------------------------------------")
        threedisplaystatus = input("Input: ")
        if threedisplaystatus == 1: print("Please select an hour to display, input an integer 08 - 24")
        threehourinput = input("Select Hour, 0 - 24: ")
        print("--------------------------------------")
        print("Please select the minute to display, input an integer 0 - 59")
        threeminuteinput = input("Select Minute: ")
        CSVHelper.resetthevalues()
        CSVHelper.resetWrongAddress()
        simulatetheentiredaygiventime(Truck2,threehourinput, threeminuteinput)
        CSVHelper.printthetable()
