from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]
