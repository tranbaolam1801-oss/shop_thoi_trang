import uuid
from django.shortcuts import redirect
from .models import HoaDonBan, ChiTietHoaDon
from apps.products.models import SanPhamChiTiet


def checkout(request):

    cart = request.session.get("cart", {})

    mahdb = str(uuid.uuid4())[:10]

    hoadon = HoaDonBan.objects.create(
        mahdb=mahdb,
        makh_id="KH001",
        tongtien=0
    )

    tongtien = 0

    for product_id, item in cart.items():

        product = SanPhamChiTiet.objects.get(pk=product_id)

        quantity = item["quantity"]

        price = 100000

        thanhtien = price * quantity

        ChiTietHoaDon.objects.create(
            mahdb=hoadon,
            maspct=product,
            soluong=quantity,
            dongiaban=price,
            thanhtien=thanhtien
        )

        # trừ tồn kho
        product.soluongton -= quantity
        product.save()

        tongtien += thanhtien


    # cập nhật tổng tiền hóa đơn
    hoadon.tongtien = tongtien
    hoadon.save()


    # ⭐ CỘNG ĐIỂM TÍCH LŨY (ĐẶT Ở ĐÂY)
    kh = hoadon.makh
    kh.diem += int(tongtien / 100000)
    kh.save()


    # xóa giỏ hàng
    request.session["cart"] = {}

    return redirect("/products")