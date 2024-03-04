#problem 1
def multiply(num):
    result = 1
    for i in num:
        result *= i
    return result

def main():
    num= input().split()
    num = [int(num) for num in num] 
    result = multiply(num)
    print("Output:", result)

if __name__ == "__main__":
    main()