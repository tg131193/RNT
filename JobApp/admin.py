from django.contrib import admin
from JobApp.models import JobPost,Noticebord

# Register your models here.
admin.site.register(Noticebord)
@admin.register(JobPost)
class JobpostAdmin(admin.ModelAdmin):

 list_display = ['id', 'job_title', 'start_date', 'last_date', 'qualifications','age_limit','job_post','job_category','state','job_borad','notification_no','is_verify']
 list_filters=('state','is_verity','job_category')

class JobappAdmin(admin.AdminSite):
     site_header='Jop Post admin'
     class Meta:

     
          list_display = ['id', 'job_title', 'start_date', 'last_date', 'qualifications','age_limit','job_post',' recruitment_post','job_category','state','job_borad','notification_no',' notice']
          exclude=('is_verify',)
          list_filters=('state','job_category')
jobpost_site=JobappAdmin('name=jobappadmin')
jobpost_site.register(JobPost)