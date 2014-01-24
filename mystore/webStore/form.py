from django import forms


class ContactForm(forms.Form):
    def clean_recipients(self):
        data = self.cleaned_data['recipients']
        if "merlion380@gmail.com" not in data:
            raise forms.ValidationError("You have forgotten about Milad!")
        return data

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")
        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise forms.ValidationError("Did not send for 'help' in "
                    "the subject despite CC'ing yourself.")

        # Always return the full collection of cleaned data.
        return cleaned_data