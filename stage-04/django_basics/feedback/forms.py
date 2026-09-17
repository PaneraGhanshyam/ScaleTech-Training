from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data["message"]

        if len(message) < 10:
            raise forms.ValidationError(
                "Message must contain at least 10 characters."
            )

        return message

