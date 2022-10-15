while(True):
    num = int(input()) 
    if(num == 0):
        break
    for i in range(num):
        if i%7 == 0:
            continue
        print(i, end = " ")
    print()    
