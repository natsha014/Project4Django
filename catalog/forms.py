import os

from django.db.models.fields import BooleanField
from django.forms import ModelForm, forms
from catalog.models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
    'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in FORBIDDEN_WORDS:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError(f'В названии нельзя использовать слово "{word}"!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in FORBIDDEN_WORDS:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError(f'В описании обнаружено запрещенное слово: "{word}"!')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной!')
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_image(self):
        image = self.cleaned_data['image']

        if not image:
            return image

        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise forms.ValidationError("Файл слишком большой! Максимальный размер — 5 МБ.")

        ext = os.path.splitext(image.name)[1]
        valid_extensions = ['.jpeg', '.png']

        if not ext.lower() in valid_extensions:
            raise forms.ValidationError("Неподдерживаемый формат! Загрузите JPEG или PNG.")

        return image
