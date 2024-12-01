from django import forms  
from products.models import Brand
class BrandForm(forms.ModelForm):  
    class Meta:  
        model = Brand  
        fields = "__all__"  