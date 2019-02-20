class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        field = ('name', 'text',)
