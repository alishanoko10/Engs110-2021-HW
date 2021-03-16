def is_prime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n,1):
        if(n%i==0):
            return False
    return True
def fibonacci(n):
    num1=0
    num2=1
    while(num1<n):
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
def binary(n):
    binarynum=""
    if (n!=0):
        while (n>=1):
            if (n%2==0):
                binarynum=binarynum+"0"
                n=n/2
            else:
                binarynum=binarynum+"1"
                n=(n-1)/2

    else:
        binarynum="0"
    return binarynum[::-1]
def main():
    num=int(input("Kindly enter a number: "))
    print("The fibonacci sequence of this number is: " )
    fibonacci(num)
    if(is_prime(num)):
        print("The number you entered is prime.")
    else:
        print("The number you entered is not a prime number.")
    print("The binary representation of this number is: " +binary(num))
main()
