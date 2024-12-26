# LibraryProject/bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, help_text="Enter the title")
    author = forms.CharField(max_length=100, required=True, help_text="Enter the author's name")
    published_date = forms.DateField(required=True, help_text="Enter the published date (YYYY-MM-DD)")

    # You can add custom validation methods if needed
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Author is required.")
        return author