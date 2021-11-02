"""
    Họ và tên: Nguyễn Văn Lộc
    Lớp: CA18A1A
    ID: 44457
    ngày: 02/11/2021
    Vấn đề:
      Câu 2 (6.0 điểm). To implement the management face of a store, people ta built a class
                        có tên là MatHang với các thông tin như sau:
     Các thuộc tính: mặt hàng mã, mặt hàng tên, số lượng, đơn giá
     Chính thức các phương thức: khởi tạo, sử dụng chỉ @properties thị cho phương thức có tên là thành tiền.
     Với: thành tiền = số lượng * đơn giá
     Câu 2.1 (1.0 điểm): Tạo một lớp với các thông tin được miêu tả như trên;
     Câu 2.2 (0,5 điểm): Tạo một menu để lựa chọn thực hiện công việc cho các công việc
                          câu sau: Câu 2.3, Câu 2.4, Câu 2.5 và Câu 2.6
     Câu 2.3 (1.5 điểm): Nhập dữ liệu vào chương trình
         Lớp dữ liệu được lưu trong văn bản đầu vào tệp, có cấu trúc như sau:
                        Mã mặt hàng | Tên hàng | Số lượng | Đơn giá
         Ví dụ một thông tin dòng cho một mặt hàng:
                        MH01 | Gạo Lài sữa | 3 | 17000
         Anh (chị) tự cho các thông tin của các mặt hàng với ít nhất 5 dòng thông tin cho 5 mặt hàng.
     Câu 2.4 (1.0 điểm): Hiển thị tất cả các thông tin của các mặt hàng ra màn hình (bao gồm tất cả thông tin về Thành tiền).
                  Trong trường hợp không có thông tin của mặt hàng, thì thông báo “Bạn cần nhập thông tin về mặt hàng”.
     Câu 2.5 (1.0 điểm): Show the information of face row have Đơn giá cao nhất ra màn hình (bao gồm cả thông tin về Thành tiền)
     Câu 2.6 (1.0 điểm): Từ các thông tin của các mặt hàng, anh (chị) hãy ghi tất cả các thông tin của các mặt hàng
                  có số lượng từ 5 trở lên (bao gồm cả thông tin về Thành tiền) ra file văn bản với mỗi mặt hàng là
                  một thông tin dòng (văn bản đầu vào tập tin tương đồng cấu trúc).
"""

def Cau2():
    data = []  # list chứa các đối tượng
    n = 0  # số lượng mặt hàng

    class MatHang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():

        #mở file
        f = open("CA20B1_VoVietThanh_58474_inp.txt", mode="r", encoding="utf-8" )

        # đọc dữ liệu đưa vào class
        n = int(f.readline())  # n là số lượng mặt hàng

        for i in range(n):
            row_data = f.readline() .split("|")
            mat_hang = MatHang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(mat_hang)  # đưa dữ liệu data vào các object

        # đóng file
        f.close()
        print("=="*10)
        print(" Hoàn thành việc nhập dữ liệu từ file: CA20B1_VoVietThanh_58474_inp.txt")

    def cv24():
        print("=="*20)
        if len(data) == 0:
            print("Bạn cần chọn thông tin về mặt hàng từ file")
        else:
            # đã có thông tin, xử lý
            print("\nIn thông tin các mặt hàng:\n")
            print("==" * 20)
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}" \
                      .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("==" * 20)

    def cv26():
        if len(data) == 0:
            print("Bạn cần chọn thông tin về mặt hàng")
        else:
            # ghi dữ liệu
            f = open("CA20B1_VoVietThanh_58474_out.txt", mode="w", encoding="utf-8")
            f.write(str(len(data)) + "\n")
            for i in data:
                s = i.ma_mat_hang + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \
                    + "|" + str(i.don_gia) +"|" + str(i.thanh_tien) + "\n"
                f.write(s)

            f.close()
        print("Hoan thanh ghi ra file CA20B1_VoVietThanh_58474_out.txt")
        print("++"*20)

    def cau25():
        """ Hiển thị mặt hàng có đơn giá cao nhất"""
        print("=== Mat Hang Dat Nhat ===")
        # tìm ra mặt hàng có đơn giá cao nhất
        matHangDatNhat = data[0]
        for i in data:
            if i.don_gia > matHangDatNhat.don_gia:
                matHangDatNhat = i
        # Hiển thị ra mặt hàng có đơn giá cao nhất
        matHangDatNhat_str = matHangDatNhat.ma_mat_hang + "|" + matHangDatNhat.ten_mat_hang + "|" + str(matHangDatNhat.so_luong) \
            + "|" + str(matHangDatNhat.don_gia) + "|" + str(matHangDatNhat.thanh_tien)
        print(matHangDatNhat_str)
        print("==" * 20)


    while True:
        print("___MENU___")
        print("1. Nhập dữ liệu từ file.")
        print("2. In dữ liệu ra màn hình.")
        print("25. In mặt hàng đơn giá cao nhất.")
        print("3. Ghi thông tin vào file.")
        cv = input("Bạn chọn công việc, bấn K để thoát: ")
        if cv == "1":
            print("call cv23")
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "25":
            cau25()
        elif cv == "3":
            cv26()
        elif cv.upper() == "K":
            break

if __name__ == '__main__':
    Cau2()