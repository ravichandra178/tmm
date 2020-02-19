from django.db import models
from quiz.models import Question
# Create your models here.

class CodeQuestion(Question):
    qtype = models.CharField(max_length = 10,default = 'code')
    
    def check_if_correct(self, guess, num):
        return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    def correct_ans(self):
        return 'Your Answer was graded already'

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Code Question"
        verbose_name_plural = "Code Questions"
    
    
class CodeAnswer(models.Model):
    question = models.ForeignKey(CodeQuestion, verbose_name='Code Question', on_delete=models.CASCADE)
    test_input = models.CharField(max_length=20,default = '')
    test_output = models.CharField(max_length=20,default = '')

    content = models.TextField(default = '',
                               blank=True,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")
    #evaluate = models.CharField(max_length = 5,default = '0.91')

    #correct = models.BooleanField(blank=False,
                                  #default=False,
                                  #help_text="Is this a correct answer?",
                                  #verbose_name="Correct")

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Code Answer"
        verbose_name_plural = "Code Answers"

