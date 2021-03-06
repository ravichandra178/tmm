from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.
from .models import Quiz, Category, Question, Progress, Profile
from mcq.models import MCQQuestion, Answer
from django.utils.translation import ugettext_lazy as _
from .models import CSVUpload
from ddq.models import DDQuestion, DDAnswer
from fitb.models import FITBQuestion ,FITBAnswer
from essay.models import Essay_Question, EssayAnswer
from codequestion.models import CodeQuestion,CodeAnswer
from drdq.models import DRDQuestion,DRDAnswer

class CSVUploadsAdmin(admin.ModelAdmin):
    model = CSVUpload
    list_display= ('title',)

class AnswerInline(admin.TabularInline):
    model = Answer

class DDAnswerInline(admin.TabularInline):
    model = DDAnswer

class DRDAnswerInline(admin.TabularInline):
    model = DRDAnswer

class FITBAnswerInline(admin.TabularInline):
    model = FITBAnswer

class EssayAnswerInline(admin.TabularInline):
    model = EssayAnswer
class CodeAnswerInline(admin.TabularInline):
    model = CodeAnswer

class QuizAdminForm(forms.ModelForm):
    """
        below is from
        http://stackoverflow.com/questions/11657682/
        django-admin-interface-using-horizontal-filter-with-
        inline-manytomany-field
    """

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ('title', 'category', )
    list_filter = ('category',)
    search_fields = ('description', 'category', )


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category', )


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'category',
              'figure', 'quiz', 'explanation', 'answer_order')

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [AnswerInline]


class ProgressAdmin(admin.ModelAdmin):
    """
    to do:
            create a user section
    """
    search_fields = ('user', 'score', )

class DDQuestionAdmin(admin.ModelAdmin):
    list_display = ('content','category', )
    list_filter = ('category',)
    fields = ('content','category',
              'figure', 'quiz', 'explanation', 'answer_order','step1','step2','step3','step4','step5','step6','step7','step8')

    search_fields = ( 'content','explanation',)
    filter_horizontal = ('quiz',)

    inlines = [DDAnswerInline]

class FITBQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'category',
              'figure', 'quiz', 'explanation', 'answer_order','qtype')

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [FITBAnswerInline]

class EssayQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'category', 'quiz', 'explanation', )
    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [EssayAnswerInline]

class CodeQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content','vid', 'category', 'quiz', 'explanation', )
    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [CodeAnswerInline]

class DRDQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'category', 'quiz', 'explanation', 'field_test1','field_choice1a','field_choice2a','field_choice3a','field_choice4a','field_test2','field_choice1b','field_choice2b','field_choice3b','field_choice4b','field_test3','field_choice1c','field_choice2c','field_choice3c','field_choice4c','field_test4')
    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [DRDAnswerInline]

admin.site.register(Essay_Question, EssayQuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MCQQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(CSVUpload, CSVUploadsAdmin)
admin.site.register(DDQuestion,DDQuestionAdmin)
admin.site.register(FITBQuestion,FITBQuestionAdmin)
admin.site.register(CodeQuestion,CodeQuestionAdmin)
admin.site.register(DRDQuestion,DRDQuestionAdmin)
admin.site.register(Profile)
