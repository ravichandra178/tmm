from django.db import models
from quiz.models import Question
# Create your models here.




ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    ('none', 'None'),
    # ('random', 'Random')
)
class DRDQuestion(Question):
    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text="The order in which multichoice \
                    answer options are displayed \
                    to the user",
        verbose_name="Answer Order")

    qtype = models.CharField(max_length = 10,default = 'drdq')
    
    field_test1 = models.TextField()
    field_choice1a = models.TextField()
    field_choice2a = models.TextField()
    field_choice3a = models.TextField()
    field_choice4a = models.TextField()

    field_test2 = models.TextField()
    field_choice1b = models.TextField()
    field_choice2b = models.TextField()
    field_choice3b = models.TextField()
    field_choice4b = models.TextField()

    field_test3 = models.TextField()
    field_choice1c = models.TextField()
    field_choice2c = models.TextField()
    field_choice3c = models.TextField()
    field_choice4c = models.TextField()

    field_test4 = models.TextField()
    

    def check_if_correct(self, guess, num):
        
            
        answer = DRDAnswer.objects.get(content=guess,question_id = num)

        if answer.correct is True:
            return True
        else:
            return False

    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        # if self.answer_order == 'random':
        #     return queryset.order_by('Random')
        if self.answer_order == 'none':
            return queryset.order_by('None')

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    class Meta:
        verbose_name = "Drop Down Question"
        verbose_name_plural = "Drop Down Questions"

    



class DRDAnswer(models.Model):
    question = models.ForeignKey(DRDQuestion, verbose_name='Question', on_delete=models.CASCADE)
    

    content = models.CharField(max_length=1000,
                               blank=True,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")
    

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a correct answer?",
                                  verbose_name="Correct")

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "DRD Answer"
        verbose_name_plural = "DRD Answers"


    
    


# Create your models here.
