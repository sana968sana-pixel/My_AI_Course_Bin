customer_name="Tin kate"
customer_age=56
customer_height=6.12
customer_age=customer_age+5 #manual way

customer_age+=5   #smart way
print(customer_name,customer_age,customer_height) 

print(type(customer_name))
print(type(customer_age))
print(type(customer_height))


sum_value=customer_age+customer_height
print("sum of age and height",sum_value)
print("type of sum value",type(sum_value))

customer_info=" tin kate is a prime customer of ABC inc. he lives in california"
print(customer_info)
print(type(customer_info))
print(len(customer_info))
for i in customer_info:  #for loop for string
    print(i)
print(customer_info[5:10])    
print(customer_info[33:40])

customer_list=["tin kate",54,6.12,"ABC Inc",True]
print(customer_list)
print(type(customer_list))
print(customer_list[1])
print(type(customer_list[1]))
print(customer_list[3])
print(type(customer_list[3]))

customer_list.append(30000)
customer_list.insert(1,"lahore")
print(customer_list)

customer_list.remove(54)
customer_list.pop(0)

print(customer_list)
print(len(customer_list))
for l in customer_list:
    print(l)
customer_list[0]="change value"
print(customer_list)

customer_tuple=("tin kate",54,6.12,"ABC Inc",True)
print("tuple len",len(customer_tuple))
for t in customer_tuple:
    print(t)
print(customer_tuple[0])
print(customer_tuple[3])
print(type(customer_tuple[0]))

customer_set={"tin kate",54,6.12,"ABC Inc",True}
print(customer_set)
print(type(customer_set))
print(len(customer_set))
for s in customer_set:
    print(s)
customer_set.add("lahore")
print(customer_set)
customer_set.discard(54)
print(customer_set)


customer_dictionary={
  "name": "tin kate",
  "age":54,
  "height":6.12,
  "company":"ABC Inc",
  "status":True
}
print(customer_dictionary)

print(type(customer_dictionary))

customer_dictionary["name"]="Tom kate"
print(customer_dictionary["name"])
customer_dictionary["university"]="nuces"
print(customer_dictionary)
for d in customer_dictionary:
    print(d)
for d in customer_dictionary:
    print(customer_dictionary[d])