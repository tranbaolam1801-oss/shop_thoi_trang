from django.db import models
from apps.users.models import KhachHang
from apps.products.models import SanPhamChiTiet


class HoaDonBan(models.Model):

    mahdb = models.CharField(max_length=10, primary_key=True)

    makh = models.ForeignKey(KhachHang, on_delete=models.CASCADE)

    ngaygio = models.DateTimeField()

    tongtien = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "HDBAN"


class ChiTietHoaDon(models.Model):

    mahdb = models.ForeignKey(HoaDonBan, on_delete=models.CASCADE)

    maspct = models.ForeignKey(SanPhamChiTiet, on_delete=models.CASCADE)

    soluong = models.IntegerField()

    dongiaban = models.DecimalField(max_digits=12, decimal_places=2)

    thanhtien = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "CHITIET_HDBAN"