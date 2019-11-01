from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from quiz.models import Question
from django.db import models


@python_2_unicode_compatible
class Essay_Question(Question):

    qtype = models.CharField(max_length = 10,default = 'essay')

    def check_if_correct(self, guess, num):
        return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    def correct_ans(self):
        #x = FITBAnswer.objects.filter(question=self,correct = True)
        #for i in x:
            #candy = i.content
        return 'Your Answer will be graded using Automated Grading System'

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Essay question")
        verbose_name_plural = _("Essay questions")



class EssayAnswer(models.Model):
    question = models.ForeignKey(Essay_Question, verbose_name='Question', on_delete=models.CASCADE)

    content = models.TextField(default = '',
                               blank=True,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")
    evaluate = models.CharField(max_length = 5,default = '0.91')

    #correct = models.BooleanField(blank=False,
                                  #default=False,
                                  #help_text="Is this a correct answer?",
                                  #verbose_name="Correct")

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
