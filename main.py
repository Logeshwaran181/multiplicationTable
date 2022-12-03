print("Welcome to VIRALO Multiplication Table Application")

class multable:
    def __init__(self,no):
        self.no = no
    def multab(self):
        for i in range (2,self.no+1):
            for j in range(1,21):
                print(i,"X",j,"=",i*j)
            print()


while (True):
    n = int(input("Enter the sentinel value : "))
    x = multable(n) #x-object
    x.multab()
    repeat = input("Do you want any other Tables ?[yes/no]:")
    if repeat != 'yes' :
        print("Come again and learn Multiplication tables.")
        break
print("Thank you")
