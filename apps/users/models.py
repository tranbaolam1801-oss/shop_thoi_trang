from django.db import models

class KhachHang(models.Model):
    makh = models.CharField(max_length=10, primary_key=True)
    tenkh = models.CharField(max_length=100)
    sdt = models.CharField(max_length=15)
    diachikh = models.CharField(max_length=200)
    diem = models.IntegerField(default=0)

    class Meta:
        db_table = "KHACHHANG"