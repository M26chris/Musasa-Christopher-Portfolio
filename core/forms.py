from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Full Name',
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email Address',
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition'
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Phone Number (optional)',
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition'
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition'
        })
    )
    service = forms.ChoiceField(
        choices=[
            ('', '-- Select a Service --'),
            ('web', 'Web Design & Development'),
            ('data', 'Data Analysis & Reporting'),
            ('cyber', 'Cybersecurity Consulting'),
            ('health', 'Health Tech Solutions'),
            ('other', 'Other / General Enquiry'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition bg-white'
        })
    )
    message = forms.CharField(
        max_length=3000,   # ← prevents spam dumps
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell me about your project or enquiry...',
            'rows': 6,
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition resize-none'
        })
    )

    # ── Honeypot field — hidden from real users, filled by bots ──
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'position:absolute; left:-9999px; top:-9999px;',
            'tabindex': '-1',
            'autocomplete': 'off'
        })
    )

    def clean_website(self):
        """Honeypot validation: if this field is filled, it's likely a bot - reject silently."""
        Value = self.cleaned_data.get('website', '')
        if Value:
            raise forms.ValidationError("Bot detected.")
        return Value