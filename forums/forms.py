from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class' : "form-control"
                })
            

class ForumForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title", "description"]
        
    def __init__(self, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class' : "form-control"
                })