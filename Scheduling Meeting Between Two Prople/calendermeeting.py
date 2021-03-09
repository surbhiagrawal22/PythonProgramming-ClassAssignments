     #### Calender Meeting ####
import datetime
from datetime import  timedelta 
import time

## Inputs for Program
MyCalender = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
MyWorkingHours = ['9:00', '20:00']
CoWorkerCalender = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30','15:00'], ['16:00', '17:00']]
CoWorkerWorkingHours = ['10:00', '18:30']
meetingDuration = 30

def convert_to_string(WorkingHour):
    # converting string to time format
    y=[]
    for i in WorkingHour :
      y.append(datetime.datetime.strptime(i, '%H:%M'))
    return y

def convert_list_of_time_string(CalenderHours):
    # converting string to time format
    y=[]
    for i in CalenderHours:
        y.append([datetime.datetime.strptime(i[0], '%H:%M'), datetime.datetime.strptime(i[1], '%H:%M')] )
    return y    

def common_working_Times(MyWorkingHours,CoWorkerWorkingHours):
    # finding common working times of both people 
    common_working_time=[]
    common_working_time.append(max(MyWorkingHours[0],CoWorkerWorkingHours[0]))
    common_working_time.append(min(CoWorkerWorkingHours[1],MyWorkingHours[1]))
    return common_working_time

def create_30_min_slots(x,meetingDuration):
    # creating 30 mins slots 
    mins30_slots=set()
    temp=x[0]
    while(temp<x[1]):
        y=temp+  timedelta(minutes=meetingDuration )
        mins30_slots.add((temp,y))
        temp=y
    return mins30_slots  

def create_30_min_slots_merged(x,meetingDuration):
    # creating 30 mins slots 
    mins30_slots=set()
    for i in x: 
       temp=i[0]
       while(temp<i[1]):
           y=temp+  timedelta(minutes=meetingDuration )
           mins30_slots.add((temp,y))
           temp=y
    return mins30_slots    


# Calling the functions to convert both Calender and Working hours to time format
CoWorkerWorkingHours=convert_to_string(CoWorkerWorkingHours)  
MyWorkingHours=convert_to_string(MyWorkingHours) 
MyCalender=convert_list_of_time_string(MyCalender)
CoWorkerCalender=convert_list_of_time_string(CoWorkerCalender)
  
# Calling the function to find both people common working hours
common_working_time=common_working_Times(MyWorkingHours,CoWorkerWorkingHours)

# Creating a set of 30 mins timeslots
Commontimeslots=create_30_min_slots(common_working_time,meetingDuration)
myCalenderTimeSlots=create_30_min_slots_merged(MyCalender,meetingDuration)
CoworkerCalenderTimeslots=create_30_min_slots_merged(CoWorkerCalender,meetingDuration)

# Using Set Operations to combine both people working slots and using diference to find the available slots
Both_people_calender_timeslots=myCalenderTimeSlots.union(CoworkerCalenderTimeslots)
avail_slots =Commontimeslots.difference(Both_people_calender_timeslots)

# Converting the result to 24 Hour Format
available_slots=[]
for i in avail_slots:
    available_slots.append([i[0].strftime("%-H:%M"),i[1].strftime("%-H:%M")])

# Printing the result  

print(f'The avaiable slots for 30 minutes duration meeting are {available_slots}')


