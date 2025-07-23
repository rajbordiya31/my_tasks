# # List
# # li=[1,2,3,4,'Raj']
# # print(li)
# # print(type(li[4]))

# # append(): Adds an element at the end of the list.
# # extend(): Adds multiple elements to the end of the list.
# # insert(): Adds an element at a specific position.

# # li.append(10)
# # print(li)

# # li.append([20,30,40])
# # print(li)

# # li.extend([20,30,40])
# # print(li)

# # li.append('Raj')
# # print(li)

# # li.extend('Raj')
# # print(li)

# # li.insert(0,6)
# # print(li)

# # remove(): Removes the first occurrence of an element.
# # pop(): Removes the element at a specific index or the last element if no index is specified.
# # del statement: Deletes an element at a specified index.

# # x=[1,2,3,4,'Raj','Bordiya',1]
# # print(x)

# # x.remove(1)
# # print(x)

# # x.pop(0)
# # print(x)

# # x.pop()
# # print(x)

# # del x[0]
# # print(x)

# # a=['Apple','Banana',1,2,3,5]
# # print(a)
# # for item in a :
# #     print(item)

# # List Comprehension
# # n=int(input("Enter the number : "))
# # squares= [x**2 for x in range (n)]
# # print(squares)

# # even =[x for x in range(1,n+1) if x%2==0]
# # print(even)

# # Dictionaries
# # dic = {"name":"Raj","age":22,"city":'Indore'}
# # print(dic)
# # print(type(dic))

# # dic["state"]="M.P"
# # print(dic)

# # dic["name"]="Nikhil"
# # print(dic)

# # del: Removes an item by key.
# # pop(): Removes an item by key and returns its value.
# # clear(): Empties the dictionary.(
# # popitem(): Removes and returns the last key-value pair.

# # del dic['age']
# # print(dic)


# # val=dic.pop('age')
# # print(val)
# # print(dic)

# # val = dic.popitem()
# # print(val)
# # print(dic)

# # dic.clear()
# # print(dic)

# # for keys in dic:
# #     print(keys)

# # for values in dic.values():
# #     print(values)

# # for key,values in dic.items():
# #     print(f"{key}:{values}")

# # Creating The modules


# import raj as r
# r.geeks()
# print(r.location)

# emp=r.Employees("Raj",25)
# emp.show()

# NESTED Dictionary

dic={
    "name":"Raj",
    "address" : {
        'city':'Indore',
        'pin':{ 'code':452001,
               'area':'Chawani'

        }
    }
}
print(dic)

def flatten_dic(d,parent_key=""):
    flat_dic = {}
    for key,value in d.items():
        new_key=parent_key +"_"+key if parent_key else key
        if isinstance(value,dict):
            flat_dic.update(flatten_dic(value,new_key))
        else:
            flat_dic[new_key]=value
    return flat_dic

flat= flatten_dic(dic)
print(flat)

