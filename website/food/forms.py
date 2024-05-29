
from django import forms
from .models import Item

'''
This is the form for entering Item' model data by user for creation,updation purpose
'''
class ItemForm(forms.ModelForm):
    
    class Meta:
        
        model = Item
        fields = ["item_name","item_description","item_price","item_image"]