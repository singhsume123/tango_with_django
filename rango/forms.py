# importing the required stuff
from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the text")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #An iniline class to provide additional information on the form.
    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of page")
    url = forms.URLField(max_length=200, help_text="Please enter the url of web page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:

        model = Page
        exclude = ('category',)