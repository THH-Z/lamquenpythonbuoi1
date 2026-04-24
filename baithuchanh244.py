print("nhap so nguyen: ");
n = int(input());

giatrituyetdoi = lambda n: abs(n);

print("gia tri tuyet doi cua", n, "la:", giatrituyetdoi(n));

socong = lambda n: n + 15;
print("so cong them 15 cua", n, "la:", socong(n));

