from django.db import models

# Create your models here.




STATE_CHOICES = (
    ('Andaman_Nicobar_Islands', 'Andaman & Nicobar Islands'),
    ('Andhra_Pradesh', 'Andhra Pradesh'),
    ('Arunachal_Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    
    ('Dadra_Nagar_Haveli', 'Dadra & Nagar Haveli'),
    ('Daman_and_Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal_Pradesh', 'Himachal Pradesh'),
    ('Jammu_Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya_Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil_Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar_Pradesh', 'Uttar Pradesh'),
    ('West_Bengal', 'West Bengal'),
    ('All', 'All India'),
    
)

CATEGORY_CHOICES = (
    ('B','Bank job'),
    ('U','Upsc job'),
    ('S','Ssc'),
    ('DF','Defence/Police Job'),
    ('R','Railways Job'),
    ('M','Medical Job'),
    ('T','Teaching Job'),
    ('E','Engineering Job'),
    
)


class JobPost(models.Model):
    job_title=models.CharField(max_length=250)
    start_date=models.DateField(blank=True)
    last_date=models.DateField( blank=True)
    qualifications=models.CharField(max_length=250,blank=True)
    age_limit=models.CharField(max_length=250,blank=True)
    job_post=models.PositiveIntegerField(blank=True)# total post
    recruitment_post=models.CharField(max_length=250,blank=True)
    job_category=models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    state=models.CharField(max_length=50,choices=STATE_CHOICES)
    job_borad=models.CharField(max_length=250,blank=True)
    job_description=models.TextField()
    notification_no=models.CharField(max_length=250,blank=True)
    notice=models.FileField(upload_to='media/notice', blank=True)
    notice_link=models.URLField( blank=True)
    apply_link=models.URLField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    is_verify=models.BooleanField(default=False)
    is_updated=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'%s   %s   %s'%(self.job_title,self.state,self.job_category)


class Noticebord(models.Model):
    notice=models.CharField(max_length=250,blank=True)
    description=models.TextField(blank=True)
    link=models.URLField(blank=True)
    is_verify=models.BooleanField(default=False )
    
    def __str__(self):
        return self.notice

class JobNatificationsMail(models.Model):
    email=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.email





   





    
         





