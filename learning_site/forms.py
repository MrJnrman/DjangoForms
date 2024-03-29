from django import forms
from django.core import validators

def must_be_empty(value):
    if value:
        raise forms.ValidationError(
            "Is not empty!"
        )

class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty", validators=[must_be_empty])

    '''
        # any function that stars with 'clean_' overrides the built in validator for django
        def clean_honeypot(self):
            # negates bots with the use of honeypot
            honeypot = self.cleaned_data['honeypot']
            if len(honeypot):
                raise forms.ValidationError(
                    "Honeypot should be left empty. Bad bot!"
                )
            return honeypot
    '''

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if email != verify:
            raise forms.ValidationError(
                'You need to enter the same email in both fields'
            )