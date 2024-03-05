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
    print(result)

if __name__ == "__main__":
    main()

#problem 2
def count(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

def main():
    user_input = input()
    upper_count, lower_count = count(user_input)
    print(upper_count)
    print(lower_count)

if __name__ == "__main__":
    main()

#problem 3
def palindrome(s):
    if s == s[::-1]:
        return 1
def main():
    s = input()
    if palindrome(s):
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()

#problem 4
import math
import time

def main():
    number = int(input())
    ms = int(input())

    time.sleep(ms / 1000)  

    sqr = math.sqrt(number)
    print(f"Square root of {number} after {ms} milliseconds is {sqr}")

if __name__ == "__main__":
    main()

#problem 5
def iftrue(tpl):
    return all(tpl)

def main():
    tpl = tuple(map(bool, input().split()))

    if iftrue(tpl):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
