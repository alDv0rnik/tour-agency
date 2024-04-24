from django import forms
from orders.models import OrderInfo


MEMBERS_NUMBER_CHOICES = [(i, str(i)) for i in range(1, 8)]


class OrderInfoEditForm(forms.ModelForm):
    members = forms.TypedChoiceField(
            choices=MEMBERS_NUMBER_CHOICES,
            coerce=int,
            label="Количество человек",
            widget=forms.Select(attrs={"class": "form-select rounded-4", "style": "max-width: 300px;"})
        )
    class Meta:
        model = OrderInfo
        fields = '__all__'
        exclude = ['order']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'city': ''
        }
        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "Имя",
                "class": "form-control rounded-4",
                "style": "max-width: 300px;"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Фамилия",
                "class": "form-control rounded-4",
                "style": "max-width: 300px;"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "form-control rounded-4",
                "style": "max-width: 300px;"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Телефон",
                "class": "form-control rounded-4",
                "style": "max-width: 300px;"
            }),
            "city": forms.TextInput(attrs={
                "placeholder": "Город",
                "class": "form-control rounded-4",
                "style": "max-width: 300px;"
            })
        }

class DatePickerInput(forms.DateInput):
    input_type = 'date'


class DateEditForm(forms.Form):
    date_from = forms.DateField(
        label="Начало",
        widget=DatePickerInput(attrs={"class": "form-control rounded-4", "style": "max-width: 300px;"})
    )
    date_to = forms.DateField(
        label="Конец",
        widget=DatePickerInput(attrs={"class": "form-control rounded-4", "style": "max-width: 300px;"})
    )
