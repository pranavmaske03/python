import multiprocessing
import time

def EvenDisplay(No):
    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print(x)
        x = x+2

def OddDisplay(No):
    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x+2     

def main():
    print("Enter number : ")
    Value = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay, args = (Value,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (Value,))
    
    p1.start()    
    p2.start()

    p1.join()
    p2.join()
    
    print("End of main process")

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Time required is : ",end - start)