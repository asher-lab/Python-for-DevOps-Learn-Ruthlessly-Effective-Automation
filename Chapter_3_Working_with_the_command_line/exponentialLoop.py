import time

def infinite(n):
    n = 1
    start = time.time()
    for i in range (9*9*2):
        n = n*n
        for i in range (10*6*n):
            n = n+1
            for i in range(n*n):
                n=n*n
                end=time.time()
                print(f"Value of i: {i}")
                print(f"Time Elapse: {end - start}")

if __name__=='__main__':
    infinite(10)
