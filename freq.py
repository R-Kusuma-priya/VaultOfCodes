str1="python java c python c python"
str1= str1.split()         
str2 = []
for i in str1:             
    if i not in str2:
        str2.append(i)  
for i in range(0, len(str2)):
    print(str2[i], 'is :', str1.count(str2[i]))    
