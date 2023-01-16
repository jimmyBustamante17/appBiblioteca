# Generated by Django 4.1.2 on 2022-11-19 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('identificador', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('cantidadRegistrada', models.PositiveIntegerField()),
                ('cantidadActual', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('idRol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBiblioteca.rol')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialPrestado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBiblioteca.usuario')),
                ('idMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBiblioteca.material')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBiblioteca.usuario')),
                ('idMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBiblioteca.material')),
            ],
        ),
    ]
