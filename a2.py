total_marks=(400)
print("enter marks obtained in 4 subjects 100/? :")
math=float(input("math:"))
science=float(input("science:"))
urdu=float(input("urdu:"))
computer=float(input("computer:"))
sum=math+science+urdu+computer
avg=(sum/4)
print("average marks=",avg)
if sum >=200:
    print("grade A+")
elif sum <=200:
    print("FAILED!")
