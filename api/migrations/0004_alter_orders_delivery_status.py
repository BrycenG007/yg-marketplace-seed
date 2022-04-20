# Generated by Django 4.0.2 on 2022-04-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cardonsale_created_at_orders_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery_status',
            field=models.CharField(choices=[('Payment approved', 'Payment approved'), ('In transit', 'In transit'), ('Finished', 'Finished')], default='Payment approved', max_length=50, verbose_name='Status'),
        ),
    ]