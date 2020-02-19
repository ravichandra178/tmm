# Generated by Django 2.1 on 2019-11-11 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0005_auto_20191101_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_input', models.CharField(default='', max_length=20)),
                ('test_output', models.CharField(default='', max_length=20)),
                ('content', models.TextField(blank=True, default='', help_text='Enter the answer text that                                             you want displayed', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Code Answer',
                'verbose_name_plural': 'Code Answers',
            },
        ),
        migrations.CreateModel(
            name='CodeQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
                ('qtype', models.CharField(default='code', max_length=10)),
            ],
            options={
                'verbose_name': 'Code Question',
                'verbose_name_plural': 'Code Questions',
            },
            bases=('quiz.question',),
        ),
        migrations.AddField(
            model_name='codeanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codequestion.CodeQuestion', verbose_name='Code Question'),
        ),
    ]
