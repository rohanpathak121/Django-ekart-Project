# Generated by Django 3.0.5 on 2020-04-30 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updatedDate', models.DateField(auto_now=True)),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]