# Generated by Django 3.1 on 2023-05-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20230415_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('PayPal', 'PayPal'), ('SSLcommerz', 'SSLcommerz')], default='Cash on Delivery', max_length=30),
        ),
    ]
