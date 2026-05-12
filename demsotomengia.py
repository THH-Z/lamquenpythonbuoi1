menhgia=[500, 200, 100, 50, 20, 10, 5, 2, 1]


def nhaptien():
    tien = int(input("Nhập số tiền: "))
    return tien

def tinhtien(tien):
    #cach 1: Dùng nhiều biến để lưu số tờ cho từng mệnh giá
    # soto500=0
    # soto200=0
    # soto100=0
    # soto50=0
    # soto20=0
    # soto10=0
    # soto5=0
    # soto2=0
    # soto1=0
    # if tien >= 500:
    #     soto500 = tien // 500  # tien -= (tien/500)*500
    #     tien = tien % 500
    # if tien >= 200:
    #     soto200 = tien // 200
    #     tien = tien % 200
    # if tien >= 100:
    #     soto100 = tien // 100
    #     tien = tien % 100
    # if tien >= 50:
    #     soto50 = tien // 50
    #     tien = tien % 50
    # if tien >= 20:
    #     soto20 = tien // 20
    #     tien = tien % 20
    # if tien >= 10:
    #     soto10 = tien // 10
    #     tien = tien % 10
    # if tien >= 5:
    #     soto5 = tien // 5
    #     tien = tien % 5
    # if tien >= 2:
    #     soto2 = tien // 2
    #     tien = tien % 2
    # if tien >= 1:
    #     soto1 = tien // 1
    #     tien = tien % 1
    # print("Số tờ 500: ", soto500)
    # print("Số tờ 200: ", soto200)
    # print("Số tờ 100: ", soto100)
    # print("Số tờ 50: ", soto50)
    # print("Số tờ 20: ", soto20)
    # print("Số tờ 10: ", soto10)
    # print("Số tờ 5: ", soto5)
    # print("Số tờ 2: ", soto2)
    # print("Số tờ 1: ", soto1)
    
    #Cach 2: Dùng vòng lặp để tính số tờ cho từng mệnh giá
    tong=0
    for i in menhgia:
        
        soto = tien // i
        tong=tong+soto
        tien = tien % i
    
        print("Số tờ ", i, ": ", soto)
    print("tong cong có : ", tong, "tờ")
    
    
def main():    
    tien = nhaptien()
    tinhtien(tien)
    
    
main()