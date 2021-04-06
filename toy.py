class LRU:
    def __init__(self,cache,capacity):#g
        self.cache = []  # it is an empty list 
        self.cache.append(cache)
        self.capacity = capacity

        

    def Set(self,a):
        if (len(self.cache) == self.capacity):
            print ("cache list is full ")
        else:
            return self.cache.append(a)
        

    def get(self):
        if (len(self.cache) == 0):
            print ("cache is empty ")
        else:
            return self.cache.pop(0)

    def display(self):
        return self.cache



def main():
    print()
    print()
    print("Enter the first URL and capacity")
    g=str(input())
    z = int(input())
    
    
    k=LRU(g,z)
    print(f"Sucessfully added the first URL:{g}")
    print()
    j=True
    while(j):
        print()
        print()
        print("Enter your desired operation:")
        print("Press 1 for setting URL into the LRU-cache")
        print("Press 2 for getting URL from the LRU-cache")
        print("Press 3 for displaying the LRU-cache")
        print("Press 0 to exit")
        n=int(input())
        if(n==1):
            print("Enter the URL to be set into the URL cache")
            x=str(input())
            print(k.Set(x))
        elif(n==2):
            print("Fetching the least recently used")
            print(k.get())
        elif(n==3):
            print("The URL's present in LRU-cache are :")
            h=[]
            h=k.display()
            print(h)
            
        elif(n==0):
            print("exit")
            j=False
        else:
            print("Invalid Input")


if __name__=="__main__":
    main()