from django.db import models

class LoaiSanPham(models.Model):
    maloaisp = models.CharField(max_length=10, primary_key=True)
    tenloaisp = models.CharField(max_length=100)

    class Meta:
        db_table = "LOAI_SANPHAM"


class SanPham(models.Model):
    masp = models.CharField(max_length=10, primary_key=True)
    tensp = models.CharField(max_length=200)
    dvt = models.CharField(max_length=20)
    maloaisp = models.ForeignKey(LoaiSanPham, on_delete=models.CASCADE)

    class Meta:
        db_table = "SANPHAM"


class Size(models.Model):
    masize = models.CharField(max_length=5, primary_key=True)
    tensize = models.CharField(max_length=20)

    class Meta:
        db_table = "SIZE"


class Mau(models.Model):
    mamau = models.CharField(max_length=5, primary_key=True)
    tenmau = models.CharField(max_length=50)

    class Meta:
        db_table = "MAU"


class SanPhamChiTiet(models.Model):
    maspct = models.CharField(max_length=15, primary_key=True)

    masp = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    masize = models.ForeignKey(Size, on_delete=models.CASCADE)
    mamau = models.ForeignKey(Mau, on_delete=models.CASCADE)

    soluongton = models.IntegerField(default=0)

    class Meta:
        db_table = "SANPHAM_CHITIET"