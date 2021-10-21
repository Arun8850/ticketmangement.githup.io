import pickle,studentpickle
print ("***WRITE file*****")
f=open('myfile.txt','w') #Create file if not exist and open it for writting
s1=input('Enter Your Text to be written in to file: ')
f.write(s1) #write text into file
f.close() #Close file
print("")
print ("***Read file *****")
f1=open('myfile.txt','r') #open file for reading
print ("Contents of file are")
s=f1.read()
print (s)
f1.close()#Close file
print("")
print ("***Append file*****")
f=open('myfile.txt','a') #open file for Appending
s2=input('Enter text to be appended in original file..')
f.write(s2)
f.close() #Close file
print("")
print ("")
print ("***Read Appended file*****")
f1=open('myfile.txt','r') #Create file if not exist and open it for reading
s=f1.read()
print (s)
f.close()
print ("***WITH OPEN*****")
with open('sample.txt','w') as f:
   s3=input('Enter text for WITHOPEN write..')
   f.write(s3)
with open('sample.txt','r') as f:
   for line in f:
       print (line)

print ("***PICKLE*****")
f3=open('studentpickle.dat','wb')
n=int(input('How many students?? '))
for i in range (n):
   roll=int(input("Enter your roll no : "))
   name=input("Enter your name : ")
   age=int(input("Enter your age : "))
   s=studentpickle.student(roll,name,age)
   pickle.dump(s,f3)
f3.close()

########## StudentPickle File################
class student:
   def _init_(self,roll,name,age):
       self.roll=roll
       self.name=name
       self.age=age
   def display(self):
       print("{:5d}{:20s}{:10.2f}".format(self.roll,self.name,self.age))