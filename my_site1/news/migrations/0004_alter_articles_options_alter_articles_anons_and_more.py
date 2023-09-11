# Generated by Django 4.2.5 on 2023-09-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_choicetopic_alter_articles_anons_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="articles",
            options={"verbose_name": "Объявление", "verbose_name_plural": "Объявления"},
        ),
        migrations.AlterField(
            model_name="articles",
            name="anons",
            field=models.CharField(max_length=250, verbose_name="Тема"),
        ),
        migrations.AlterField(
            model_name="articles",
            name="date",
            field=models.DateTimeField(verbose_name="Дата размещения"),
        ),
        migrations.AlterField(
            model_name="articles",
            name="full_text",
            field=models.TextField(verbose_name="Объявление"),
        ),
        migrations.AlterField(
            model_name="articles",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Категория"),
        ),
    ]