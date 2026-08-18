from django import forms

from myPosts.models.CreatePostModel import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic','title','imagePost', 'content']
        widgets = {
            'imagePost': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
