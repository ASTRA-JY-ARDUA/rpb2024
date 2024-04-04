

def add(x, y):
    
    return x + y

def subtract(x, y):
   
    return x - y

def multiply(x, y):
    
    return x * y

def divide(x, y):
    
    if y == 0:
        raise ValueError("나누는 수는 0이 될 수 없습니다.")
    return x / y

def main():
    print("연산자를 선택해주세요:")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    
    choice = input("선택 (1/2/3/4): ")
    
    num1 = float(input("첫 번째 숫자: "))
    num2 = float(input("두 번째 숫자: "))
    
    if choice == '1':
        print("결과:", add(num1, num2))
    elif choice == '2':
        print("결과:", subtract(num1, num2))
    elif choice == '3':
        print("결과:", multiply(num1, num2))
    elif choice == '4':
        try:
            print("결과:", divide(num1, num2))
        except ValueError as e:
            print("에러:", e)
    else:
        print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
