#ii. Cho nhập 2 chuỗi (S1 và S2).

#a) In ra những ký tự xuất hiện trong cả 2 chuỗi.

#Gợi ý: sử dụng class Counter trong module collections để chuyển mỗi chuỗi vào 1 dict thuộc class Counter. Thực hiện phép và (&) trên 2 dict này để có kết quả.

#b) Đếm xem có bao nhiêu ký tự có trong S1 nhưng không có trong S2 và có trong S2 nhưng không có trong S1.

#c) In ra những ký tự có trong S1 nhưng không có trong S2 và những ký tự có trong S2 nhưng không có trong S1.

#Gợi ý: đưa mỗi chuỗi vào 1 dict (dict1 và dict2). Thực hiện dò tìm S1 trên dict2 và tìm S2 trên dict1.

def ky_tu_chung(s1, s2):
    from collections import Counter
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    chung = counter1 & counter2
    return list(chung.elements())
print("Nhap chuoi S1:")
s1 = input()    
print("Nhap chuoi S2:")
s2 = input()
print("Cac ky tu xuat hien trong ca 2 chuoi la:", ky_tu_chung(s1, s2))

print("So luong ky tu co trong S1 nhung khong co trong S2 la:", len(set(s1) - set(s2)))
print("So luong ky tu co trong S2 nhung khong co trong S1 la:", len(set(s2) - set(s1)))



print("Cac ky tu co trong S1 nhung khong co trong S2 la:", set(s1) - set(s2))
print("Cac ky tu co trong S2 nhung khong co trong S1 la:", set(s2) - set(s1))

