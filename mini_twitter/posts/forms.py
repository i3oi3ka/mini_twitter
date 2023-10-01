from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']
        widgets = {
            'user': forms.Select(attrs={'class': 'form+-control'}),
            'post': forms.Select(attrs={'class': 'form+-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }