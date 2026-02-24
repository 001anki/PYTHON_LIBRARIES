import numpy as np

#[Row X Column], [3 X 3] Matrix
#In here rows are particular student's Result and columns are particular subject
Marks=np.array([
    [65,70,98],#Student 01(Row 1)
    [30,34,50],#Student 02(Row 2)
    [29,71,95]# Student 03(Row 3)
])#  s1,s2,s3

print("Marks of the student1: ",Marks[1])#This will print the marks of the Student 02 (Prints Whole row, located in index num 1)

print(Marks[1,2])#This will print the marks of the 3rd Subject of the Student 2(Here 1 is row index, 2 is Column index)

print(Marks[:])#This will print whole Matrix

total=np.sum(Marks[0])
print("\nTotal Marks of student-1 Scored: ",total)# This will print the total marks of the student 1

total=np.sum(Marks[1])
print("\nTotal Marks of student-2 Scored: ",total)# This will print the total marks of the student 2

total=np.sum(Marks[2])
print("\nTotal Marks of student-3 Scored: ",total)# This will print the total marks of the student 3

print("\nStudents with Marks Scored less than 35 are: ")
for i in range(3):#This will be row index
    for j in range(3):#This will be column index
        if(Marks[i,j]<35):#This will check each matrix index if condition statisfies or not
            print("Student:",i+1,"Subject:",j+1,"Marks:",Marks[i,j])#This will print Marks of the matched condition

print("\nMark of the sub1: \n",Marks[:,0].reshape(-1,1))#This will print all the Marks of the particular subject in column format

print("\nStudents with Marks Scored Distinction(>95) are: ")
for i in range(3):#This will be row index
    for j in range(3):#This will be column index
        if(Marks[i,j]>95):#This will check each matrix index if condition statisfies or not
            print("Student:",i+1,"Subject:",j+1,"Marks:",Marks[i,j])#This will print Marks of the matched condition

# n=int(input("Enter your choice:\n1.Marks of the all"))
# while(1):
#     if