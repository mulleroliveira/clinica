from django.db import models

class Cliente(models.Model):

    sexo_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    nome = models.CharField(max_length=50)
    dt_nasc = models.DateField(verbose_name='Data De Nascimento')
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=sexo_choices)

class Medico(models.Model):

    sexo_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    escolaridade_choices = (
        ('Graduação', 'Graduação'),
        ('Pós-Graduação', 'Pós-Graduação'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
        ('pós-doutorado', 'pós-doutorado')

    )

    nome = models.CharField(max_length=50)
    data_nasc = models.DateField(verbose_name='Data De Nascimento')
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    peso = models.DecimalField(max_digits=3, decimal_places=1)
    tamanho = models.DecimalField(max_digits=3, decimal_places=2)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=11)
    grau_instrução = models.CharField(max_length=15, choices=escolaridade_choices, verbose_name='Nivel De Escolaridade')