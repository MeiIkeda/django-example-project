from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('migrations', '0001_initial')]

    operations = [
        migrations.DeleteModel('AlcoholicProduct'),
        migrations.AddField('Author', 'rating', models.IntegerField(default=0)),
    ]
