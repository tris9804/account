# Generated by Django 3.0 on 2019-12-16 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proportion',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='percent', to=settings.AUTH_USER_MODEL, verbose_name='所有人'),
        ),
        migrations.AddField(
            model_name='consume',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Category', verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='consume',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid', to=settings.AUTH_USER_MODEL, verbose_name='付款人'),
        ),
        migrations.AddField(
            model_name='category',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='accounts.AccountBook', verbose_name='所屬帳簿'),
        ),
        migrations.AddField(
            model_name='authority',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='accounts.AccountBook', verbose_name='帳本'),
        ),
        migrations.AddField(
            model_name='authority',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share', to=settings.AUTH_USER_MODEL, verbose_name='使用者'),
        ),
        migrations.AlterUniqueTogether(
            name='authority',
            unique_together={('user', 'book')},
        ),
    ]
