# Generated by Django 2.0.12 on 2019-09-30 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddq', '0002_auto_20190926_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddquestion',
            name='step1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ddquestion',
            name='step8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
