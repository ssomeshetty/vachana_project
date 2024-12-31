from django import forms
from .models import Vachana
from authors.models import Author

class VachanaForm(forms.ModelForm):
    class Meta:
        model = Vachana
        fields = ['author', 'category', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, exclude authors from the form if you want the user to select their own
        self.fields['author'].queryset = Author.objects.all()  # Limit to available authors
