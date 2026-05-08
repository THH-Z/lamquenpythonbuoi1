

fileObject = open("D:\Downloads\Text.txt", "r", encoding="utf-8")
print(fileObject.read())
#to do xuat ra file van ban mới giảm dung lượng lưu trữ so với file gốc
list = fileObject.readlines()
print(list)
fileObject.close()
    
    
# def cau2():
#     fileObject = open("D:\Downloads\Text.txt", "r", encoding="utf-8")
#     print(fileObject.read())   
#     #doc file sau khi giam dung luong luu tru và trả về file gốc để so sánh dung lượng lưu trữ
#     fileObject.close()
    