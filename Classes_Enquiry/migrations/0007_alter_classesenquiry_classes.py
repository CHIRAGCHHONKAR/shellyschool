# Generated by Django 4.2.3 on 2023-08-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes_Enquiry', '0006_alter_classesenquiry_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classesenquiry',
            name='Classes',
            field=models.CharField(choices=[('Hospitality, Leisure & Sports Courses', 'Hospitality, Leisure & Sports Courses'), ('Environmental Studies & Earth Sciences', 'Environmental Studies & Earth Sciences'), ('Natural Sciences & Mathematics Courses', 'Natural Sciences & Mathematics Courses'), ('Basic English Speaking and Grammar', 'Basic English Speaking and Grammar')], max_length=100, null=True),
        ),
    ]
