from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
    sender = forms.EmailField(required=False)

    def clean_confirmpass(self):
        copass = self.cleaned_data['confirmpass']
        password = self.cleaned_data['password']
        if copass != password:
            raise forms.ValidationError(u"رمز ورود با رمز تایید برابر نیست")
        return copass




    def clean_subject(self):
        sender = self.cleaned_data['subject']
        if sender=='':
            raise forms.ValidationError('لطفا نام خود را وارد کنید')
        return sender

    def clean_message(self):
        sender = self.cleaned_data['message']
        if sender=='':
            raise forms.ValidationError('لطفا نظر خود را وارد کنید')
        return sender

    def clean_sender(self):
        sender = self.cleaned_data['sender']
        if sender=='':
            raise forms.ValidationError('لطفا میل خود را وارد کنید')
        return sender



    def clean(self):
        cleaned_data = super(ContactForm, self).clean()



        # Always return the full collection of cleaned data.
        return cleaned_data


