car_info={'car1':{'id':1, 'name': 'bmw', 'rent': 5000, 'status': 'available'},
        'car 2':{'id': 2, 'name': 'punch', 'rent': 2000, 'status': 'availble'}
        }

for i in car_info.values():
    print(i)
print("This car is available")

x=input("Enter your name: ")
y=int(input("Enter car id: "))
z=int(input("Enter no of hours: "))

cust_info=dict()
cust_info['name']=x
cust_info['id']=y
cust_info['hours']=z

print(cust_info)

for i in car_info.values():
    for j,k in i.items():
        if k==y:
            r=i['rent']*z

billinfo=dict()
billinfo['CustName']=x
billinfo['CarId']=y
billinfo['RentforCar']=r
billinfo['DurationforRented']=z

print("Bill_Info = ",billinfo)