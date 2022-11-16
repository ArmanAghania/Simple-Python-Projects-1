import statistics
name_A = input("Name: ")
c = 'Go On'
a = []
s = float(input('Enter Your Grade:'))
a.append(s) 
m = round(statistics.mean(a), 2)
while c == 'Go On':
 
    cc = input('if you are done, type: "exit", if NOT, enter your next score :')
    if cc == 'exit':
        break
    else:
        s = float(cc)
        a.append(s) 
        m = round(statistics.mean(a), 2)

print(m)
    
if m >= 17:
    print(name_A, "Your Average is: ", m, "- Great")     
elif m < 17 and m >= 12:
    print(name_A, "Your Average is: ", m, "- Average")
else:
    print(name_A, "Your Average is: ", m, "- Failed")

