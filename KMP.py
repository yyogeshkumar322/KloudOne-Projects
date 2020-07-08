print("Enter the str:")
s1=input()
print("Enter the Pattern to search:")
pattern=input()
pt= [0]*len(pattern)
j=0
i=1
c=0
pt[0]
while i < len(pattern):
    if pattern[i]== pattern[c]:
        c+= 1
        pt[i] = c
        i += 1
    else:
        if  c!= 0: 
            c = pt[c-1]
        else:
            pt[i] = 0
            i += 1
i = 0 
while i < len(s1): 
    if pattern[j] == s1[i]:
        i += 1
        j += 1
    if j == len(pattern):
        print("searching pattern found at position: " + str(i-j))
        j = pt[j-1] 
  
    elif i < len(s1) and pattern[j] != s1[i]: 
        if j != 0: 
            j = pt[j-1] 
        else:
            i += 1
