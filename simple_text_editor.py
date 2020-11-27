"""
implement a simple text editor. Initially, your editor contains an empty string, . You must perform operations of the following

types:

    append

- Append string to the end of
.
delete
- Delete the last characters of
.
print
- Print the character of
.
undo
- Undo the last (not previously undone) operation of type or , reverting to the state it was in prior to that operation. 


"""

dic={0:''};order=0;s=''
for i in range(int(input())):
  t = input().strip().split()
  if t[0]=='1':order+=1;s+=t[1];dic[order]=s
    
  elif t[0]=='3':print(s[int(t[1])-1])
  
  elif t[0]=='2':s=s[:len(s)-int(t[1])];order+=1;dic[order]=s
  
  elif t[0]=='4':order-=1;s=dic[order]

