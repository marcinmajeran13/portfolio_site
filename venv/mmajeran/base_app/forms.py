from django import forms
from base_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'emailfield'}))
    subject = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'subjectfield'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'emailfield'}), required=True)



# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#
#     pass