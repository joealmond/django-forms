from dataclasses import fields
from django import forms

from.models import Review


# class ReviewsForm(forms.Form):
#     user_name = forms.CharField(label="Your name:", max_length=50, error_messages={
#         "required": "Your name must not be empty!",
#         "max_lenght": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(
#         label="Your feedback:", widget=forms.Textarea, max_length=150)
#     rating = forms.IntegerField(label="Your Rating:", min_value=1, max_value=5)

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  # or ["user_name", "review_text", "rating"]
        # exclude = ["owner_comment"] # for only the exceptions
        labels = {
            "user_name": "Your name:",
            "review_text": "Your feedback:",
            "rating": "Your rating:"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_lenght": "Please enter a shorter name!"
            }
        }
