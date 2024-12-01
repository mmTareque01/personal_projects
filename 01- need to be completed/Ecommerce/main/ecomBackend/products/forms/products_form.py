from django import forms  
from products.models import Products, Categories
class ProductsForm_x(forms.ModelForm):  

    class Meta:  
        model = Products  
        fields = "__all__"  


class ProductsForm(forms.ModelForm):
    # Create a custom queryset to fetch category names
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), to_field_name="name")

    class Meta:
        model = Products
        fields = ['name', 'image', 'price', 'stock', 'category', 'brand', 'meta_data']