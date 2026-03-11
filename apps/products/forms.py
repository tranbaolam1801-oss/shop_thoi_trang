from django import forms
from .models import SanPham

class SanPhamForm(forms.ModelForm):

    class Meta:
        model = SanPham
        fields = "__all__"