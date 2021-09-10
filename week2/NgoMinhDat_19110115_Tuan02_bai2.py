def tinhGiaiThuaCuaSoNguyenDuong():
    num = 0
    while num <= 0:
        num = float(input('Nhap so duong:'))
    rs = 1
    for x in range(1, int(num) + 1):
        rs = rs * x
    print(str(rs))
    return rs


tinhGiaiThuaCuaSoNguyenDuong()
