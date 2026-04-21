from datetime import *
# #I1: Viết chương trình hiển thị thông tin về thời gian hiện tại, bao gồm năm, tháng, tuần, ngày, giờ, phút, giây. 
print("Năm hiện tại:",datetime.now().strftime("%Y"));
print("Tháng hiện tại:",datetime.now().strftime("%b"));
print("tuần hiện tại là tuần thứ mấy trong năm:",datetime.now().strftime("%W"));
print("tuần hiện tại là tuần thứ mấy trong tháng:",datetime.now().strftime("%u"));
print("Ngày hiện tại là ngày thứ mấy trong năm:",datetime.now().strftime("%j"));
print("Nhày dương lịch hiện tại:",datetime.now().strftime("%x"));
print("thứ cua ngày hiện tại:",datetime.now().strftime("%A"));
print("giờ phút giây hiện tại:",datetime.now().strftime("%X"));

#I2: Yêu cầu người dùng nhập vào hai ngày và tính khoảng cách giữa hai ngày đó.
print("Nhap ngày thang nam cua hai ngay (dd/mm/yyyy):");
ngay1 = input("Ngay 1: ");
ngay2 = input("Ngay 2: ");
ngay1 = datetime.strptime(ngay1, "%d/%m/%Y");   #dinh dang cho ngay thang nam la: ngay/thang/nam
ngay2 = datetime.strptime(ngay2, "%d/%m/%Y");   #dinh dang cho ngay thang nam la: ngay/thang/nam
print("Khoang cach giua hai ngay la: " + str(abs((ngay2 - ngay1).days)) + " ngay");

# #I3: Hiển thị lịch của một tháng cụ thể.
chuoingaythang_string = input("nhap chuoi có dang thang/ngay/nam/gio: ");
dt = datetime.strptime(chuoingaythang_string, "%b %d %Y %H:%M%p");
print(dt);

#I4 sử dụng datetime.timedelta để thêm 5 giây vào thời gian hiện tại và hiển thị kết quả.
print("Thời gian hiện tại:", datetime.now());
new_time = datetime.now() + timedelta(seconds=5);
print("Thời gian sau khi thêm 5 giây:", new_time);



# import calendar
# print( calendar.monthcalendar(2026, 4));
