# Generated by Django 4.0.4 on 2022-05-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_category',
            field=models.CharField(choices=[('B', 'Bank job'), ('U', 'Upsc job'), ('S', 'Ssc'), ('DF', 'Defence/Police Job'), ('R', 'Railways Job'), ('M', 'Medical Job'), ('T', 'Teaching Job'), ('E', 'Engineering Job')], max_length=50),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='state',
            field=models.CharField(choices=[('Andaman_Nicobar_Islands', 'Andaman & Nicobar Islands'), ('Andhra_Pradesh', 'Andhra Pradesh'), ('Arunachal_Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Dadra_Nagar_Haveli', 'Dadra & Nagar Haveli'), ('Daman_and_Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal_Pradesh', 'Himachal Pradesh'), ('Jammu_Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya_Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil_Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar_Pradesh', 'Uttar Pradesh'), ('West_Bengal', 'West Bengal'), ('All', 'All India')], max_length=50),
        ),
    ]
