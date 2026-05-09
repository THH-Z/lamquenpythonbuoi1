import os

# Sử dụng 'r' trước chuỗi đường dẫn (raw string) để tránh lỗi với dấu backslash (\)
file_goc = r"D:\Downloads\Text.txt"
file_moi = r"D:\Downloads\Text_Reduced.txt"

def tao_file_giam_dung_luong():
    """Đọc file gốc, xóa khoảng trắng thừa và dòng trống, sau đó lưu ra file mới"""
    try:
        with open(file_goc, "r", encoding="utf-8") as f_in:
            lines = f_in.readlines()
        
        with open(file_moi, "w", encoding="utf-8") as f_out:
            for line in lines:
                cleaned_line = line.strip() # Xóa khoảng trắng và ký tự xuống dòng thừa
                if cleaned_line:            # Nếu dòng không trống thì mới ghi vào
                    f_out.write(cleaned_line + "\n")
                    
        print(f"Đã tạo file mới tại: {file_moi}")
    except FileNotFoundError:
        print("Không tìm thấy file gốc! Vui lòng kiểm tra lại đường dẫn.")

def cau2():
    """So sánh dung lượng của file gốc và file mới"""
    # Kiểm tra xem cả 2 file đã tồn tại chưa
    if not os.path.exists(file_goc) or not os.path.exists(file_moi):  #os.path.exists() kiểm tra sự tồn tại của file (os là thư viện để làm việc với hệ thống file) os là "cầu nối" giúp code Python của bạn có thể giao tiếp và ra lệnh cho hệ điều hành (Windows, macOS, hoặc Linux) đang chạy máy tính .
        print("Lỗi: Không tìm thấy file để so sánh!")
        return

    # Lấy dung lượng file (tính bằng bytes)
    size_goc = os.path.getsize(file_goc)
    size_moi = os.path.getsize(file_moi)
    
    # Tính toán mức độ giảm
    giam_duoc = size_goc - size_moi
    phan_tram_giam = (giam_duoc / size_goc * 100) if size_goc > 0 else 0

    print("\n--- KẾT QUẢ SO SÁNH DUNG LƯỢNG ---")
    print(f"Dung lượng file gốc: {size_goc} bytes")
    print(f"Dung lượng file mới: {size_moi} bytes")
    print(f"Đã tiết kiệm được:   {giam_duoc} bytes ({phan_tram_giam:.2f}%)")

# --- Thực thi chương trình ---
tao_file_giam_dung_luong()
cau2()