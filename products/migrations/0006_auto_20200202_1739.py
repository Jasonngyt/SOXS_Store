# Generated by Django 2.2.6 on 2020-02-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200202_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
