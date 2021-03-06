# Generated by Django 2.1 on 2020-02-19 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0005_auto_20191101_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='DRDAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, help_text='Enter the answer text that                                             you want displayed', max_length=1000, verbose_name='Content')),
                ('correct', models.BooleanField(default=False, help_text='Is this a correct answer?', verbose_name='Correct')),
            ],
            options={
                'verbose_name': 'DRD Answer',
                'verbose_name_plural': 'DRD Answers',
            },
        ),
        migrations.CreateModel(
            name='DRDQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
                ('answer_order', models.CharField(blank=True, choices=[('content', 'Content'), ('none', 'None')], help_text='The order in which multichoice                     answer options are displayed                     to the user', max_length=30, null=True, verbose_name='Answer Order')),
                ('qtype', models.CharField(default='drdq', max_length=10)),
                ('field_test1', models.TextField()),
                ('field_choice1a', models.TextField()),
                ('field_choice2a', models.TextField()),
                ('field_choice3a', models.TextField()),
                ('field_choice4a', models.TextField()),
                ('field_test2', models.TextField()),
                ('field_choice1b', models.TextField()),
                ('field_choice2b', models.TextField()),
                ('field_choice3b', models.TextField()),
                ('field_choice4b', models.TextField()),
                ('field_test3', models.TextField()),
                ('field_choice1c', models.TextField()),
                ('field_choice2c', models.TextField()),
                ('field_choice3c', models.TextField()),
                ('field_choice4c', models.TextField()),
                ('field_test4', models.TextField()),
            ],
            options={
                'verbose_name': 'Drop Down Question',
                'verbose_name_plural': 'Drop Down Questions',
            },
            bases=('quiz.question',),
        ),
        migrations.AddField(
            model_name='drdanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drdq.DRDQuestion', verbose_name='Question'),
        ),
    ]
