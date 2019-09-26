from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=50, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'text-center',
#                 'placeholder' : 'ENTER TITLE'
#             }
#         )
#         )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'ENTER CONTENT',
#                 'rows' : 10,
#                 'cols' : 30,
#             }
#         )
#         )

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title'
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'ENTER CONTENT',
                'rows' : 10,
                'cols' : 30,
            }
        )
    )

    class Meta:
        model = Article
        # fields = ('title', 'content',)
        fields = '__all__'
        # exclude = ('title',)
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'
        #     })
        # }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)
