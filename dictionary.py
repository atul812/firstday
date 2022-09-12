d= {"Name":"Atul", "Age":18, "Followers":12, "Occupation":"Student"}

# for i in d.keys():
# #     print(d[i])
# print(type(d))
# # print(d.keys())
# # print(d.values())
# print(d["Name"])
# # print(d["Age"])
# d[False]="I am sorry"
# print(d)
# d.update({"hobby":"writing"})
# print(d)
# del d["hobby"]
# print(d)
# d.clear()
# print(d)

def ping(n):
    if (n%2==0):
        return True

    return False

def printing(num):
    val=ping(num)
    if (val==True):
        print("Number is Even")
    else:
        print("Number is odd")

number=int(input())
printing(number) 