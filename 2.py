y=input("Melanie Dental Clinic")
print("",y)
print("*_____________*")

print("What is patient name")
x=input("enter the patient" )
print("",x)

print("Has the patient been here before?")
y=input("enter yes or no")
print("",y)

print("What is the patient’s height (in cm)?")
z=int(input( "enter the height in cm"))
print("",z,"cm")

print("What is the patient’s weight (in kg)?")
a= float(input("enter the weight in kg"))
print("",a,"kg")

print("When was the patient last weighed in (1/1/2000 if never weighed)? (date)")
b=input("enter the date when weighted")
print("",b)

print("What was the patient’s weight (in kg, -1 if never weighed)? (float)")
c=float(input("enter the weight of a person last weighted"))
print("",c,"kg")

print("Practitioner’s overall assessment of the patient’s health (-5=very poor to +5=excellent, 0 for neutral) (int)")
f=int(input("enter overall assessment of patient health"))
if f>0:
    print("excellent")
elif a==0:
    print("neutral")
elif a<0:
    print("very poor")
