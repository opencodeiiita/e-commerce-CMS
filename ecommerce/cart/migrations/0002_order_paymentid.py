from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymentId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]