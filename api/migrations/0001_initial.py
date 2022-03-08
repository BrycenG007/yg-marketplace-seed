# Generated by Django 4.0.2 on 2022-02-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=100, verbose_name='Name')),
                ('card_attribute', models.CharField(max_length=20, verbose_name='attribute')),
                ('card_level', models.IntegerField(verbose_name='Level/Rank/Link')),
                ('card_type', models.CharField(max_length=100, verbose_name='Type')),
                ('card_description', models.TextField(verbose_name='Effect/Description')),
                ('card_atk', models.IntegerField(blank=True, null=True, verbose_name='ATK')),
                ('card_def', models.IntegerField(blank=True, null=True, verbose_name='DEF')),
                ('card_ability', models.CharField(blank=True, max_length=10, null=True, verbose_name='Other')),
            ],
        ),
    ]