# 2. Write a program to define the UDF
#  a. To calculate the factorial
#  b. To generate a fibonacci series upto 'n' term [recursive function]

# ==========================================
# Core Functions (Unchanged)
# ==========================================

def fact(n):
    sum = 1
    while n != 1:
        sum = sum * n
        n -= 1
    return sum


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print("--- Math Operations Menu ---")
print("1. Calculate Factorial")
print("2. Generate Fibonacci Series")
choice = input("Enter your choice (1 or 2): ").strip()

print("-" * 28)

if choice == "1":
    num = int(input("Enter any non-negative whole number for Factorial --> "))
    
    if num == 0:
        facts = 1
    else:
        facts = fact(num)
        
    print(f"The factorial of {num} is: {facts}")

elif choice == "2":
    num = int(input("Enter the number of terms for Fibonacci series --> "))
    print(f"Fibonacci series up to {num} terms:")
    for i in range(num):
        print(fib(i), end="\t")
    print()

else:
    print("Invalid choice! Please run the program again and select either 1 or 2.")