price={"дети":0, "молодые":990, "взрослые":1390}
a=0
b=0
c=0
n=int(input("введите количество билетов:\n"))

for i in range(0,n):
 age = int(input("Введите возраст посетителя:\n"))
 if age<18:
    a=a+1
 elif 18<=age<=25:
    b=b+1
 else:
    c=c+1
total_cost=a*price.get("дети")+b*price.get("молодые")+c*price.get("взрослые")
if n>3:
    total_cost=total_cost*0.9
print(total_cost)