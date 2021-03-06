from django import forms
from django.forms.widgets import RadioSelect, TextInput
from django.utils.safestring import SafeData, SafeText, mark_safe
from .models import Profile


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

class DDQForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(DDQForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(widget=TextInput(attrs={'style': 'width:100%'}))

class FITBForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(FITBForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(widget=TextInput(attrs={'style': 'width:100%'}))

class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:100%'}))

class DRDForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(DRDForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(widget=TextInput(attrs={'style': 'width:100%'}))


class CodeForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(CodeForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:100%'}))    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'   


