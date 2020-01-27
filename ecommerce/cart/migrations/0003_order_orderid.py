from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_paymentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
