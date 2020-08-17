 ## Recursive Solution 
def Fibonacci(n): 
    if n<0: 
        # the first input must be 0
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
   
  

 ## Recursive Solution 

def lucas(n) : 
      
    # Base cases  
    if (n == 0) : 
        return 2
    if (n == 1) : 
        return 1
  
    # the  relation  
    return lucas(n - 1) + lucas(n - 2)





def sum_series(n, first=0, second=1):
    #Determine nth number in series 
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)

"""
## another solution for sum_series function :

def sum_series(n, first=0, second=1):
  
    if first == 0 and second == 1:
        return Fibonacci(n)
    elif first == 2 and second == 1:
        return lucas(n)
    else :
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)

    """

    
