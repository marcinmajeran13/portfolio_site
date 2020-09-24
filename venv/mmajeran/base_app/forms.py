from base_app.models import Post, App
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'type']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'description', 'image', 'github_link', 'other_link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'emailfield'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'subjectfield'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'messagefield'}), required=True)
