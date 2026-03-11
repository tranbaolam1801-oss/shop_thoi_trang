from django.db import models
from apps.products.models import SanPhamChiTiet


class HoaDonNhap(models.Model):

    mahdn = models.CharField(max_length=10, primary_key=True)

    ngaygio = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "HDNHAP"


class ChiTietNhap(models.Model):

    mahdn = models.ForeignKey(HoaDonNhap, on_delete=models.CASCADE)

    maspct = models.ForeignKey(SanPhamChiTiet, on_delete=models.CASCADE)

    soluong = models.IntegerField()

    dongianhap = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "CHITIET_HDNHAP"