n = float(input("Nhap so duong n: "))
sole = 0;
sochan = 0;
while n>0:
    sodau = n % 10
    n = n // 10
    print ("Chu so dau tien la: ", sodau)  
    if (sodau % 2 != 0):
        sole+=1;
    else:
        sochan+=1;
        
        
print ("So le cua so la: ", sole);
print ("So chan cua so la: ", sochan);        
        
        

        