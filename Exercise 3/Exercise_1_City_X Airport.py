
class Airport:
    def __init__(self,name):
        self.name=name
       
Airport1=Airport("A1")
Airport2=Airport("A2")
Airport3=Airport("A3")
Airport4=Airport("A4")
Airport5=Airport("A5")

# dictionary of original landing with all initalised to zero.
dict1={Airport1.name:0,Airport2.name:0,Airport3.name:0,Airport4.name:0,Airport5.name:0}

class Airline:

    def __init__(self,name,origin,originaldestination,finaldestination) :
        self.name=name 
        self.origin=origin
        self.originaldestination=originaldestination
        self.finaldestination=finaldestination
    
    def no_of_emergency_landing(self):
        self.no_of_emergency_landings=0
        emr_landing=0   # temp variable for if condition
        emr_landing1=0   # temp1 variable for el

        
        for i in range(len(self.origin)):

            if (self.origin[i]==self.finaldestination[i] ):  #  check for emergeency landing at source itself 

                   self.no_of_emergency_landings=self.no_of_emergency_landings+1
                  
                   emr_landing = dict1[self.origin[i]] + 1

                   dict1.update({self.origin[i]:emr_landing})
                   


            elif  (self.originaldestination[i]!=self.finaldestination[i]):

                   self.no_of_emergency_landings=self.no_of_emergency_landings+1
                  
                   emr_landing1 = dict1[self.finaldestination[i]] + 1

                   dict1.update({self.finaldestination[i]:emr_landing1})     

        

##################################################################################
##  Flight Name       ## Source      ## originaldestination    ## final destination
##################################################################################
##  Turkish           ## Airport1    ## Airport2                ## Airport4  (emergency landing)
                      ## Airport2    ## Airport1                ## Airport 3  (emergency landing)
                      ## irport3     ## Airport2                ## Airport3    (emergency landing)
#-------------------------------------------------------------------------------#
##  Luftsana          ## Airport2    ## Airport1                ## Airport 2    ( emergency landing)
#-------------------------------------------------------------------------------#
##   Emirates         ## Airport1    ## Airport3                ##  Airport1  ( not an emergency)
                      ## Airport1    ## Airport4                ##  Airport1 (emergency landing))

##################################################################################

turkish=Airline("Turkishairways",[Airport1.name,Airport2.name,Airport3.name],[Airport2.name,Airport1.name,Airport2.name],[Airport4.name,Airport3.name,Airport3.name])
Lufthansa=Airline("Lufthanaairways",[Airport2.name],[Airport1.name],[Airport2.name])
emirates=Airline("emirates",[Airport1.name,Airport1.name],[Airport3.name,Airport4.name],[Airport3.name,Airport1.name])


turkish.no_of_emergency_landing()
emirates.no_of_emergency_landing()
Lufthansa.no_of_emergency_landing()

# to print airport with maximim emergerncy landing 

max_key=max(dict1,key=dict1.get)
print(f'The airport with maximum landing is {max_key} with {dict1[max_key]} landing ')

# to print airlines with maximim emergerncy landing 

dict2= {turkish.name:turkish.no_of_emergency_landings,Lufthansa.name:Lufthansa.no_of_emergency_landings,emirates.name:emirates.no_of_emergency_landings}
max_key1=max(dict2,key=dict2.get)
print(f'The airline with maximum landing is {max_key1} with {dict2[max_key1] } landings ')




