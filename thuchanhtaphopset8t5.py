# bài 3 Viết chương trình nhập vào một số điện thoại, sau đó in ra các chữ số có trong số điện thoại đó và các chữ số không có trong số điện thoại đó.

print("Nhập số điện thoại của bạn:");
sdt = input();
set_sdt = set(sdt);
setsonguyen = set("0123456789");
print(setsonguyen - set_sdt);
print("Các chữ số có trong số điện thoại của bạn là:", set_sdt);

#
