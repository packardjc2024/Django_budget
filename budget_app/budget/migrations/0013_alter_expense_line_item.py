# Generated by Django 5.1 on 2024-08-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0012_alter_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='line_item',
            field=models.CharField(choices=[('gas', 'Gas'), ('Food', 'Food'), ('Internet', 'Internet'), ('Phone', 'Phone'), ('Electric', 'Electric'), ('Trash', 'Trash'), ('Mortgage', 'Mortgage'), ('Child Care', 'Child Care'), ('Insurance', 'Insurance')], default='Food', max_length=20),
        ),
    ]
