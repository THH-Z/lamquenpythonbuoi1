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