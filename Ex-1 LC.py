''' 
Write a python program to implement Linear 
Congruential algorithm to generate five pseudo 
random numbers.
'''
def linearcongruential(x,m,a,c,rand,randcount):
    rand[0]=x
    for i in range(1,randcount):
        rand[i]=(((rand[i-1]*a)+c)%m)

if __name__=="__main__":
    x=5
    m=7
    a=3
    c=3
    randcount=5
    rand=[0]*(randcount)
    linearcongruential(x,m,a,c,rand,randcount)
    for i in rand:
        print(i,end=" ")