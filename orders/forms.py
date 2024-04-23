from django import forms

from orders.models import OrderInfo


class OrderInfoEditForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = '__all__'
