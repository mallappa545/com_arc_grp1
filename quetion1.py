#Singed Binary Arthematic using 8-bit2'compliment
'''def to_binary(n):
    return formation(n&255,'08b')

def binary_add(a,b):
    carry=0
    result=""

    for i in range(7,-1,-1):
        total=int(a[i]+b[i])+carry
        result=str(total%2)+result
        carry=total//2

    return result,carry

def calculate(a,b):
    A=to_binary(a)
    B=to_binary(b)

    result,carry=binary_add(A,B)

    decimal_result=result_to_decimal(result)

    overflow=(a>=0)==(b>=0)and((decimal_result>=0)!=(a>=0))

    print("\nOperand 1:",a,"=",A)
    print("Operand 2:",b,"=",B)
    print("Binary addition:")
    print("",A)
    print("+",B)
    print("-----------")
    print("",result)
    print("Carry out:",carry)
    print("Decimal result:",decimal_result)
    print("Overflow:","Yes"if overflow else "No")

def result_to_decimal(binary):
    value=int(binary,2)

    if binary[0]=='1':
        value-=256

    return value

print("SIGNED BINARY ARITHMETIC")
print("\n(a)25+(+18)")
calculate(25,18)

print("\n(b)(-25)+(-18)")
calculate(-25,-18)'''
# Signed Binary Arithmetic using 8-bit 2's Complement

def to_binary(n):
    return format(n & 255, '08b')


def binary_add(a, b):
    carry = 0
    result = ""

    for i in range(7, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        result = str(total % 2) + result
        carry = total // 2

    return result, carry


def calculate(a, b):
    A = to_binary(a)
    B = to_binary(b)

    result, carry = binary_add(A, B)

    decimal_result = result_to_decimal(result)

    # Signed overflow occurs when operands have
    # the same sign but result has a different sign.
    overflow = (a >= 0) == (b >= 0) and (
        (decimal_result >= 0) != (a >= 0)
    )

    print("\nOperand 1:", a, "=", A)
    print("Operand 2:", b, "=", B)
    print("Binary addition:")
    print(" ", A)
    print("+", B)
    print("-----------")
    print(" ", result)
    print("Carry out:", carry)
    print("Decimal result:", decimal_result)
    print("Overflow:", "Yes" if overflow else "No")


def result_to_decimal(binary):
    value = int(binary, 2)

    if binary[0] == '1':
        value -= 256

    return value


print("SIGNED BINARY ARITHMETIC")
print("\n(a) 25 + (+18)")
calculate(25, 18)

print("\n(b) (-25) + (-18)")
calculate(-25, -18)
