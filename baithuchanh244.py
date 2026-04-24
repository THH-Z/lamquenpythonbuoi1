print("nhap so nguyen: ");
n = int(input());

#a)
giatrituyetdoi = lambda n: abs(n);
print("gia tri tuyet doi cua", n, "la:", giatrituyetdoi(n));

#b)
socong = lambda n: n + 15;
print("so cong them 15 cua", n, "la:", socong(n));

#c)
print("nhap so nguyen x: ");
x = int(input());
print("nhap so nguyen y: ");
y = int(input());
sotich = lambda x, y: x * y;
print("so tich cua", x, "va", y, "la:", sotich(x, y));

#d)
boiso = lambda n: n % 13 != 0 and n % 19 != 0;
if boiso(n):
    print(n, "khong chia het cho 13 va 19");
    
#e)
print("nhap so ban kinh duong tron r: ");
r = int(input());
dientich = lambda r: 3.14 * r * r;
print("dien tich cua duong tron la:", f"{dientich(r):.2f}");

#f)
print("nhap chieu dai: ");
dai = int(input());
print("nhap chieu rong: ");
rong = int(input());
chuv = lambda dai, rong: 2 * (dai + rong);
print("chu vi cua hinh chu nhat la:", chuv(dai, rong));

#g)
sochinhphuong = lambda n: n ** 2;
print("so chinh phuong cua", n, "la:", sochinhphuong(n));

#h)
songuyento = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1));
if songuyento(n):
    print(n, "la so nguyen to");
    
#i)
xettamgiac = lambda a, b, c: (a + b > c) and (a + c > b) and (b + c > a);
kiemtraloaitamgiac = lambda a, b, c: "tam giac deu" if a == b == c else "tam giac can" if a == b or b == c or a == c else "tam giac thuong";
print("nhap canh a: ");
a = int(input());
print("nhap canh b: ");
b = int(input());
print("nhap canh c: ");
c = int(input());
if xettamgiac(a, b, c):
    print("3 canh", a, b, c, "tao thanh tam giac");
    print("Loai tam giac:", kiemtraloaitamgiac(a, b, c));
else:   
    print("3 canh", a, b, c, "khong tao thanh tam giac");

