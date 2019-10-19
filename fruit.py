data=[]
with open('C:/Users/ASUS/Desktop/food.txt','r') as f:
    for oo in f:
        data.append(oo.strip())
print(data)
        