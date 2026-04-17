print ("Nhap chieu dai cua hinh hop chu nhat: ");
n = float(input('nhap gia tri chieu dai: '));
print ("Nhap chieu rong cua hinh hop chu nhat: ");
m = float(input('nhap gia tri chieu rong: '));
print ("Nhap chieu cao cua hinh hop chu nhat: ");
h = float(input('nhap gia tri chieu cao: '));


sole = input('so le cua hinh hop chu nhat: ');
dinhdang = '{:.'+sole+'f}';  #hien thi so le phia sau dua tren so le mìnhh nhap vao



print ("dien tich day hinh chu nhat =",float(dinhdang.format(n * m)),"cm\u00b2");
print ("dien tich hinh khoi =",float(dinhdang.format(n * m * h)),"cm\u00b2");

