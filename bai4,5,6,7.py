n = float(input("Nhap so duong n: "))
sole = 0;
sochan = 0;
tong = 0;
tich = 1;
solonnhat = -1;
solocphat = True;
while n>0:
    sodau = n % 10
    n = n // 10
    tong += sodau
    tich *= sodau
    if sodau > solonnhat:
        solonnhat = sodau
    #print ("Chu so dau tien la: ", sodau)  
    if (sodau != 6 and sodau != 8):
        solocphat = False
        break;
    
    if (sodau % 2 != 0):
        sole+=1;
    else:
        sochan+=1;
    
if solocphat:
    print ("\nSo loc phat");
else:
    print ("\nSo khong loc phat");

print ("\nChu so lon nhat la: ", solonnhat);
print ("\nTong cac chu so la: ", tong);
print ("\nTich cac chu so la: ", tich);
print ("\nSo le cua so la: ", sole);
print ("\nSo chan cua so la: ", sochan);        
        
        

        