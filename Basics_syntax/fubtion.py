def fun(num):
    for x in range(1,num+1):
        print( str(x) +'+' +str(x)+ '='+ str(2*x) )
def suM(num):
    total=0
    for x in range(1,num+1):
        total+=x
    return total
print (suM(1000000))
