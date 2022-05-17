infile=open("t.txt",'r')
outfile=open("faesal.txt","w")
s=infile.read()
s=s.splitlines()
c=0
infile.close()
for i in s:
   a=input(i[:-1])
   if a==i[-1]:
       c+=1
       print("true")

name=input("name: ")
print(name,c)
outfile.write(name+str(c))
outfile.close()
