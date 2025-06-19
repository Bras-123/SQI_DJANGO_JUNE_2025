from django import forms

# reviews/forms.py (New file)
class ReviewForm(forms.Form):
    reviewer_name = forms.CharField(
        label="Your Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        help_text="Enter a rating between 1 and 5.",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'})
    )
    comment = forms.CharField(
        label="Comment",
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})
    )



