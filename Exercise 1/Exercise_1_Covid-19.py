import random
import datetime

class cityX:

    batch_size=5

    # class method to change batch size in future with a given value
    @classmethod
    def change_batch_size(cls,value):
        cls.batch_size=value

    # initalse the list of patients :
    def __init__(self,recoveredlist):
        self.recoveredlist=recoveredlist

    # to add new covid -19 patient in the list 
    def __add__(self,new_patient):
        self.recoveredlist.extend(new_patient)  

   # to know the number of patients in the list 
    def __len__(self):
        return len(self.recoveredlist)

    def __repr__(self):
        return f'The number of current recovered patients as of now is {len(self.recoveredlist)}'    

# regular method to print testdate of patients
    def test_date(self,value):
         self.test_date={}
         for i in value:
             print(f'Patient {i[0]} is tested on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
             self.test_date.update({f'{i[0]}':f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'})
         return self.test_date
 
# regular method to select patients based on batch size

    def random_choose_patient(self):

        # dividing the group of patients depending on batch size
        chunks = [list1.recoveredlist[x:x+cityX.batch_size] for x in range(0, len(list1.recoveredlist), cityX.batch_size)]
        list_of_random_patients=[]

        for random_subset in chunks:
           x=random.sample(random_subset,1)
           list_of_random_patients.append(x)

        return list_of_random_patients  



list1=cityX(['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15',
'p16','p17','p18','p19','p20'])    

# randomly choose 4 patients from batch size of 5
list_of_random_patients =list1.random_choose_patient()
print(f'the list of randomly chosen pateints is {list_of_random_patients}')

# print the datetime of test date of randomly chosen 4 patients from batch size of 5
print(list1.test_date(list_of_random_patients))
print(list1.__repr__())



