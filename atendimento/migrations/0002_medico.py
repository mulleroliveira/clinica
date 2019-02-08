# Generated by Django 2.1.3 on 2018-11-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('sexo', models.CharField(max_length=1)),
                ('peso', models.DecimalField(decimal_places=1, max_digits=3)),
                ('tamanho', models.DecimalField(decimal_places=2, max_digits=3)),
                ('email', models.EmailField(max_length=30)),
                ('telefone', models.CharField(max_length=11)),
                ('grau_instrução', models.CharField(max_length=50)),
            ],
        ),
    ]