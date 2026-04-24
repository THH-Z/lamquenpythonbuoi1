#dùng đệ quy tính tổng các chữ số của một số nguyên dương n

def tong_chu_so(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + tong_chu_so(n // 10)

print("nhap so nguyen duong: ")
n = int(input())
print("tong cac chu so cua", n, "la:", tong_chu_so(n));

def giaithua(n):
    if n==1:
        return 1
    else:
        return giaithua(n-1)*n
    
print("gia thua cua ",n,"la", giaithua(n));


print("Nhap a");
a = int(input());
print("Nhap b");
b = int(input());


def amub(a,b):
    if b==0:
        return 1
    return amub(a,b-1)*a

print("luy thua",a,"^",b,"=",amub(a,b));
    

def gcd(a,b):
    if  b == 0:
        return  a 
    return gcd(b,a % b )
print("uoc so chung lon nhat la: ",gcd(a,b))

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(n));