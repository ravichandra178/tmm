from django.db import models
from quiz.models import Question
# Create your models here.


ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    ('none', 'None'),
    # ('random', 'Random')
)
class DDQuestion(Question):
    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text="The order in which multichoice \
                    answer options are displayed \
                    to the user",
        verbose_name="Answer Order")

    qtype = models.CharField(max_length = 10,default = 'ddq')
    
    #step1 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step2 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step3 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step4 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step5 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step6 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step7 = models.ImageField(upload_to = 'snips/',blank=True,null=True)
    #step8 = models.ImageField(upload_to = 'snips/',blank=True,null=True)

    step1 = models.CharField(max_length = 100,blank=True, null=True)
    step2 = models.CharField(max_length = 100,blank=True, null=True)
    step3 = models.CharField(max_length = 100,blank=True, null=True)
    step4 = models.CharField(max_length = 100,blank=True, null=True)
    step5 = models.CharField(max_length = 100,blank=True, null=True)
    step6 = models.CharField(max_length = 100,blank=True, null=True)
    step7 = models.CharField(max_length = 100,blank=True, null=True)
    step8 = models.CharField(max_length = 100,blank=True, null=True)
    

    def check_if_correct(self, guess, num):
        
            
        #r = DDAnswer.objects.filter(
        answer = DDAnswer.objects.get(content=guess,question_id = num)

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
        return self.order_answers(DDAnswer.objects.filter(question=self))

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in self.order_answers(DDAnswer.objects.filter(question=self))]

    def answer_choice_to_string(self, guess):
        return str(guess)
        #return DDAnswer.objects.get(id=guess).content
    def correct_ans(self):
        x = DDAnswer.objects.filter(question=self,correct = True)
        for i in x:
            candy = i.content
        return candy

    class Meta:
        verbose_name = "Drag Drop Question"
        verbose_name_plural = "Drag Drop Questions"

    


class DDAnswer(models.Model):
    question = models.ForeignKey(DDQuestion, verbose_name='Question', on_delete=models.CASCADE)

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
        verbose_name = "DD Answer"
        verbose_name_plural = "DD Answers"


    
    
