"""
    Họ và tên: Nguyễn Văn Lộc
    Lớp: CA18A1A
    ID: 44457
    Vấn đề:
      Câu 1 (2.0 điểm). Viết hàm trong tiền tố số trong khoảng từ 30 đến 200

"""

def  Cau1 ():
    def  snt ( n ):
        "" "Kiểm tra so nguyen thành" ""
        f  =  Đúng
        cho  j  trong  phạm vi ( 2 , n ):
            nếu  n  %  j  ==  0 :
                f  =  Sai
                nghỉ
        trả lại  f

    def  in_snt ( a = 30 , b = 200 ):
        print ( "Danh sach so nguyen to:" )
        "" "Kiem tra so nguyen to trong khoang tu a den b" ""
        cho  tôi  trong  phạm vi ( a , b  +  1 ):
            nếu  snt ( i ):
                print ( i , end = "" )
        print ()

    # thực thi phần nguyên tố tim
    in_snt ( 30 , 200 )


if  __name__  ==  '__main__' :
    Cau1 ()
