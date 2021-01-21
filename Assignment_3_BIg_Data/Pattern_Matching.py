from  string import punctuation
def check_star(string2):
      string3 = ''
      for l in range(len(string2)):
            if string2[l] == '*':
                  string3 += string2[l-1]
            else:
                string3 += string2[l]
      if string2[len(string2)-1] == '*':
            string3 += string3[len(string3)-1]
      return string3          
def checkfunc(string1,string2,m=0,n=0):
    if string2[0] == '*' and len(string2) == 1:
          return True
    else:
          string2=check_star(string2) 
    if string1==string2:
          return True
    if len(string1) > len(string2) and string2[0]== '.':
          return False
    for k in range(len(string1)):
          strcomp=checkstr(m,n,string1,string2)
          if strcomp :
              m = m+1
              n = n+1
              continue
          else:
            p = n+1
            if len(string2[p:]) >= len(string1):
                string2=string2[p:]
                return checkfunc(string1,string2)
    return strcomp
def checkstr(i,j,string1,string2):
      if string1[i]==string2[j]:  # if both strings are equal 
        return True
      elif string1[i]!=string2[j] and string2[j] == '.':
        return True
      else:
        return False     



print(checkfunc(string1='aab', string2='.*'))  # test case 3 runned succesfully
print(checkfunc('aba', 'ab.'))
print(checkfunc('aba', '*ab')) # Test case 1 runned succesfully
print(checkfunc('aa', 'a*')) # Test case 2 runned succesfully
print(checkfunc('ab', '.*')) # Test case 3 runned succesfully
print(checkfunc('ab', '.')) # Test case 4 runned succesfully
print(checkfunc('aab', 'c*a*b'))
print(checkfunc('aaa', 'a*'))



