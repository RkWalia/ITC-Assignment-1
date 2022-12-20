#Ques2

gross_income=int(input("Please enter your Gross Income:"))
no_of_dependents=int(input("Enter number of Dependent People:"))
dependent_deduction=3000
standard_deduction=10000

taxable_income=gross_income - standard_deduction - (dependent_deduction*no_of_dependents)

tax_rate=0.2
tax=taxable_income*tax_rate

print("Tax: ",tax)