                          ### Box Stacking ####
Sample_input=[[2, 1, 2], [2, 2, 8], [1, 3, 1], [2, 3, 4], [4, 4, 5], [3, 2, 3],[1,1,1],[20,2,10]]

# Sorting the disks in decreasing order of surface area

Sample_input.sort(key=lambda x:x[0]*x[1] ,reverse=True)
 
finalheighttracker={}  # an empty dictionary to hold heights and the combination of disks
for i in range(len(Sample_input)):
      
   heightstack=[]  # to hold the heights
   boxstack=[]  
   temp=Sample_input[i] 
   boxstack.append(temp)
   heightstack=temp[2]

   for j in range(i+1,len(Sample_input)) :

        if  temp[0]>Sample_input[j][0] and temp[1]>Sample_input[j][1]:       
             temp =   Sample_input[j] 
             boxstack.append(temp)
             heightstack=heightstack+temp[2]

   finalheighttracker.update({heightstack:boxstack})
 
## printing the result 

print(f'The highest possible height of  stack is {max(finalheighttracker.keys())} and the possible combination is {finalheighttracker[max(finalheighttracker.keys())]} ')