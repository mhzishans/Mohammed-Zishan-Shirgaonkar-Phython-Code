print("Date: 27/01/26, UIN: 251A015")

BS=int(input("enter your base salary: "))
DS=0.7*BS
print("The dearness allowance is: ",DS)
TA=0.3*BS
print("The travel allowance is: ",TA)
HRA=0.1*BS
print("The house rent allowance is: ",HRA)
Gross_salary=BS+DS+TA+HRA
print("The Gross salary is: ",Gross_salary)
