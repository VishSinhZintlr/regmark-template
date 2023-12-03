from django import forms

class DataUploadForm(forms.Form):
    product_id = forms.CharField(label='Product ID', max_length=100)
    data_sheet_id = forms.CharField(label='Data Sheet ID', max_length=100)
    table_id = forms.CharField(label='Table ID', max_length=100)
    file = forms.FileField()
