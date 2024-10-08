
from collections import defaultdict

s = "ADOBECODEBANC"
t = "ABC"
s=list(s)
i,j=0,1
min_sub = s
sub_array =[]

def check_if_valid(array):
    if set(t)-set(array):
        return False
    return True

i,j=0,1
while i<len(s):
    sub_array=s[i:j]
    flag=check_if_valid(sub_array)
    if flag:
        i+=1
        print(sub_array,i,j,min_sub)
        if len(sub_array)<len(min_sub):
            # print("before",min_sub)
            min_sub=sub_array
            # print("after",min_sub)
        while s[i] not in t:
            i+=1
    else:
        j+=1
print(min_sub)