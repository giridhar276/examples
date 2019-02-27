

#for val in range(1,100):
#    print("192.168.0." + str(val))
#    
#    
#fixed = "192.168.0."
#for val in range(1,100):
#    ip = fixed + str(val)
#    print(ip)

 
fixed = "192.168."

for val in range(0,2):
    subip = fixed + str(val)
    for val in range(1,100):
        print(subip +"." + str(val))
        
######
# OR   
#####
list1 = []
list2 = []
fixed = "192.168."
for val in range(1,100):
    list1.append(fixed + "0." + str(val))
    list2.append(fixed + "1." + str(val))
    
for ip in list1:
    print(ip)
for ip in list2:
    print(ip)