from datetime import date
from .models import SanPhamChiTiet
from django.db import connection


def get_discount(product_id):

    today = date.today()

    query = """
    SELECT MUCGIAM
    FROM KHUYENMAI km
    JOIN SANPHAM_KHUYENMAI spkm
    ON km.MAKM = spkm.MAKM
    WHERE spkm.MASPCT=%s
    AND %s BETWEEN NGAYBATDAU AND NGAYKETTHUC
    """

    with connection.cursor() as cursor:

        cursor.execute(query,[product_id,today])

        row = cursor.fetchone()

        if row:
            return row[0]

    return 0