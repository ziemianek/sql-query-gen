from django import forms


class PromptForm(forms.Form):
    prompt = forms.CharField(
        label="Your prompt",
        max_length=2000,
        widget=forms.Textarea(
            attrs = {
                'class': 'input-prompt',
                }
            )
        )
