from django.shortcuts import render
from django.db.models import Sum
from apps.orders.models import HoaDonBan, ChiTietHoaDon
from apps.products.models import SanPhamChiTiet


def dashboard(request):

    doanhthu = HoaDonBan.objects.aggregate(
        Sum("tongtien")
    )

    best = ChiTietHoaDon.objects.values(
        "maspct"
    ).annotate(
        total=Sum("soluong")
    ).order_by("-total")[:5]

    tonkho = SanPhamChiTiet.objects.filter(
        soluongton__lt=10
    )

    return render(request,"dashboard.html",{
        "doanhthu":doanhthu,
        "best":best,
        "tonkho":tonkho
    })