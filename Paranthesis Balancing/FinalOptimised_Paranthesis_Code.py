#### PROGRAM TO RETURN LONGEST BALANCES STRING  ######
## https://hub.docker.com/repository/docker/surbhidocker1/pythonparanthesis ##
## Docker link :https://hub.docker.com/layers/surbhidocker1/pythonparanthesis/latest/images/sha256-1fb0e0ee0542bde950bed2042fd8112bb78bb44a83f751021461b09b4160f428?context=explore ##
""" ORIGINAL CODE HERE AND BELOW OPTIMISED CODE
# initialise empty list for storing temp results 

openingbraces=[]  # stack to push opening braces when they appear while parsing list
indexes=[]        # stack to store indexes of popped opening brackes and closing bracket 
openingindex=[]   # stack to store index of only opening braces
distances=[]      # make use of indexes list and calculate the distnace bw opening nad closing brackets
pairlist=[]       # stack to store popped opening braces and new closing braces as a pair
def Paranthesisbalancing(s) :           
 for i in range(len(s)):
    if s[i]=="{":
        # push each opeing bracket in a stack called openingbraces
        openingbraces.append(s[i])
        openingindex.append(i)   # push the index of each opening braces into the stack called openingindex
               
    elif s[i]=="}"  : 
        if  len(openingindex)!=0 and  len(openingbraces)!=0:      # check if the opening braces is not empty  ,then only append         
             indexes.append((openingindex.pop(),i))    # append the index of opening closing braces in stack called indexes
             pairlist.append((openingbraces.pop(),s[i]) )

s=input("Please enter a string for which you want longest balance string")

Paranthesisbalancing(s)  # calling the function Paranthesisbalancing

if indexes:
 for i in indexes:
    distances.append(i[1]-i[0])
else:
    pass  

if distances  :
 pos=distances.index(max(distances))
 print(f'The longest string is  {s[  indexes[pos][0]:indexes[pos][1]+1   ]} and length is {len(s[  indexes[pos][0]:indexes[pos][1]+1   ])}') 
else :
    print("The string is not balanced")

"""
## Code optimisation done by removing two lists and space complexity is reduced.####
"""
1) openingbraceslist has been removed, as there is no need to append the opening braces in a different stack. A we are already keeping track of the indexes of opening braces as occured in a stack called openingindex.
2) pairlist has been removed as there is no need to keep the pair of opening and closing braces in a pairlist .As we are already storing indexes of pair of opening and closing braces in indexes stack.
Therefore, the use of two unnecesaary list has been removed.

Considering n is the length of the string .We will traverse the whole string to check the paranthesis.

Therefore Time complexity will be in terms of length of the string
>Time Complexity: O(n)  same has been verified using strat time and end time ,when longer string was given ,it took more time to parse the list 

>Space Complexity:

1) If we have a valid string like "{{{}}}"

Then the Space complexity is O(n/2) as the openingindex list will store the indexes of all opening brackets till it traverses half the length of the string and then it starts to pop out .
Since O(n/2) , where 1/2 is insignificant , we can say
Space Complexity (worst case when string is valid) =O(n) 

2) If we have a invalid string of all opening brackets like "{{{{{{{{{"
Space Complexity (worst case when string is invalid) =O(n)
as it will store the indexes of all the opening brackets in openingindex and none of the index will be pop out , as ot will has no corresponding closing brackets.

3) Good case will be when string is like "{}{}{}"
Then whenever a index of opening brackets is pushed , it will be immediately popped out
initialise empty list for storing temp results """

import time
import memory_profiler
from memory_profiler import profile

starttime=time.time()
indexes=[]       # list to store indexes of opening/closing pairs
openingindex=[]
distances=[] 
s="{{{}{{}{{}{{}}}}}}{{{{{{{}}}}}{}{{{{{}}{{}{}{{{{}{{}}{}}}{{{{{}{{}{{{}{{}}}}}}}{{}}}}}{}}{}}}}}}{{{}}{}{}}"
# @profile
def Paranthesisbalancing(s) :           
  for i in range(len(s)):
     if s[i]=="{":
            openingindex.append(i)   # store index of each opening bracket
     elif s[i]=="}"  : 
        if  len(openingindex)!=0  :      # check if the opening braces is not empty  ,then only append         
            indexes.append((openingindex.pop(),i))    # append the index of opening closing braces in stack called indexes
  if indexes:
     for i in indexes:
        distances.append(i[1]-i[0])
  else:
        pass  

  if distances  :
       pos=distances.index(max(distances))
       print(f'The longest string is  {s[  indexes[pos][0]:indexes[pos][1]+1   ]} and length is {len(s[  indexes[pos][0]:indexes[pos][1]+1   ])}') 
       print("\n")    
  else :
       print("The string is not balanced") 
       print("\n")           
 
Paranthesisbalancing(s)  # calling the function Paranthesisbalancing

endtime=time.time()
print("\n")
print(f'Time taken to run the program is {endtime-starttime}')



