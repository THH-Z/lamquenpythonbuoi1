#Viet chuong trinh nhap nhieu lan cac so nguyen duong, sau moi  lan nhap , chuong trinh se hoi nguoi dung co muon tiep tuc nhap hay khong (yes/no). neu chon yes (y) thi cho nguoi dung nhap tiep, neu chon no (n) chuong trinh se thuc hien:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True         

numbers = []
while True: 
    print("Nhap so nguyen duong: ")
    num = int(input())
    if num > 0:
        numbers.append(num)
    else:
        print("Vui long nhap so nguyen duong.")
        continue
    print("Ban co muon tiep tuc nhap khong? (yes/no)")
    cont = input().lower()
    if cont == 'no' or cont == 'n':
        #a. in ra cac so nguyen to co trong list
        prime_numbers = [n for n in numbers if is_prime(n)]
        print("Cac so nguyen to trong list la:", prime_numbers)
        
        #b. tinh trung binh cong cac so am, trung binh cac so duong
        am_numbers = [n for n in numbers if n < 0]
        duong_numbers = [n for n in numbers if n > 0]   
        
        #c. so long nhat va so nho nhat trong list
        if numbers:
            max_num = max(numbers)
            min_num = min(numbers)
            print("So lon nhat trong list la:", max_num)
            print("So nho nhat trong list la:", min_num)
            
        #d. cho biet cac so list co duoc sap xep theo thu tu tang dan hay chua
        if numbers == sorted(numbers):
            print("Cac so trong list da duoc sap xep theo thu tu tang dan.")
        break

