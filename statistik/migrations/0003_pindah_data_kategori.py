from django.db import migrations

MAPPING_LAMA = {
    'PENDIDIKAN': 'Pendidikan',
    'PEKERJAAN': 'Pekerjaan',
    'USIA': 'Kelompok Usia',
    'AGAMA': 'Agama',
}

def pindahkan_data(apps, schema_editor):
    DataStatistik = apps.get_model('statistik', 'DataStatistik')
    KategoriStatistik = apps.get_model('statistik', 'KategoriStatistik')

    for old_key, new_name in MAPPING_LAMA.items():
        kategori_obj, created = KategoriStatistik.objects.get_or_create(nama_kategori=new_name)
        DataStatistik.objects.filter(kategori=old_key).update(kategori_baru=kategori_obj)

class Migration(migrations.Migration):

    dependencies = [
        ('statistik', '0002_kategoristatistik_alter_datastatistik_options_and_more'), 
    ]

    operations = [
        migrations.RunPython(pindahkan_data),
    ]