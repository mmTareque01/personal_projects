from django import forms  
from products.models import Categories
class CategoriesForm(forms.ModelForm):  
    class Meta:  
        model = Categories  
        fields = "__all__"  