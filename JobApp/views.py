from urllib import request
from django.shortcuts import render
from django.views import View
from JobApp.models import JobPost,Noticebord
# Create your views here.
class Jobview(View):

    def get (self,request): 

        job=JobPost.objects.all().filter(is_verify=True)[:10]
        notice=Noticebord.objects.all().filter(is_verify=True)[:10]
       
        return render(request,"index.html",{'job':job,'notice':notice})




#job category
def jobcategory(request,data=None):
    jobs_category=""
    job_name=""
    number_of_job=0.0

    if data==None:

        jobs_category=JobPost.objects.filter(job_category="B").filter(is_verify=True)

        
        
    elif data=="bank":
        jobs_category=JobPost.objects.filter(job_category='B').filter(is_verify=True)
        number_of_job=len(jobs_category)
       
        job_name='Bank jobs'
    elif data=="Upsc":
        jobs_category=JobPost.objects.filter(job_category='U').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='UPSC jobs'
        
    elif data=="SSC":
        jobs_category=JobPost.objects.filter(job_category='S').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='Ssc jobs'
        
    elif data=="Defence":
        jobs_category=JobPost.objects.filter(job_category='DF').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='defence / police jobs'
        
    elif data=="Railways":
        jobs_category=JobPost.objects.filter(job_category='B').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='Railways jobs'
        
    elif data=="medical":
        jobs_category=JobPost.objects.filter(job_category='M').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='Medical jobs'
        
    elif data=="traching":
        jobs_category=JobPost.objects.filter(job_category='T').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='Treacher Jobs'
        
    elif data=="engineering":
        jobs_category=JobPost.objects.filter(job_category='E').filter(is_verify=True)
        number_of_job=len(jobs_category)
        job_name='Engineering jobs'
  
    return render(request,'jobpage.html',{'jobs_category':jobs_category,'job_name':job_name,'number_of_job':number_of_job}) 

#job category
def statejob(request,data=None):
    state_job=[]
    job_name=""
   

    if data=='Andaman_Nicobar_Islands':

        state_job=JobPost.objects.filter(state='Andaman_Nicobar_Islands').filter(is_verify=True)
        job_name='Andaman Nicobar Islands'

        
        
    elif data=="Andhra_Pradesh":
        state_job=JobPost.objects.filter(state='Andhra _Pradesh').filter(is_verify=True)
        
        job_name='Andhra Pradesh'
    elif data=="Arunachal_Pradesh":
        state_job=JobPost.objects.filter(state='Arunachal_Pradesh').filter(is_verify=True)
       
        job_name='Arunachal Pradesh'
        
    elif data=="Assam":
        state_job=JobPost.objects.filter(state='Assam').filter(is_verify=True)
        
        job_name='Assam'
        
    elif data=="Bihar":
        state_job=JobPost.objects.filter(state='Bihar').filter(is_verify=True)
        
        job_name='Bihar'
        
    elif data=="Chandigarh":
        state_job=JobPost.objects.filter(state='Chandigarh').filter(is_verify=True)
        
        job_name='Chandigarh'
        
    elif data=="Dadra_Nagar_Haveli":
        state_job=JobPost.objects.filter(state='Dadra_Nagar_Haveli').filter(is_verify=True)
        
        job_name='Dadra Nagar Haveli'
        
    elif data=="Daman_and_Diu":
        state_job=JobPost.objects.filter(state='Daman_and_Diu').filter(is_verify=True)
       
        job_name='Daman and Diu'
        
    elif data=="Delhi":
        state_job=JobPost.objects.filter(state='Delhi').filter(is_verify=True)
       
        job_name='Delhi'
    elif data=="Goa":
        state_job=JobPost.objects.filter(state='Goa').filter(is_verify=True)
       
        job_name='Goa'

    elif data=="Gujarat":
        state_job=JobPost.objects.filter(state='Gujarat').filter(is_verify=True)
        job_name='Gujarat'
       
    elif data=="Haryana":
        state_job=JobPost.objects.filter(state='Haryana').filter(is_verify=True)
        job_name='Haryana'
       
    elif data=="Himachal_Pradesh":
        state_job=JobPost.objects.filter(state='Himachal_Pradesh').filter(is_verify=True)
        job_name='Himachal Pradesh'
       
    elif data=="Jammu_Kashmir":
        state_job=JobPost.objects.filter(state='Jammu_Kashmir').filter(is_verify=True)
        job_name='Jammu Kashmir'
       
    elif data=="Jharkhand":
        state_job=JobPost.objects.filter(state='Jharkhand').filter(is_verify=True)
        job_name='Jharkhand'
       
    elif data=="Karnataka":
        state_job=JobPost.objects.filter(state='Karnataka').filter(is_verify=True)
        job_name='Karnataka'
       
    elif data=="Kerala":
        state_job=JobPost.objects.filter(state='Kerala').filter(is_verify=True)
        job_name='Kerala'
       
    elif data=="Lakshadweep":
        state_job=JobPost.objects.filter(state='Lakshadweep').filter(is_verify=True)
        job_name='Lakshadweep'
       
    elif data=="Madhya_Pradesh":
        state_job=JobPost.objects.filter(state='Madhya_Pradesh').filter(is_verify=True)
        job_name='Madhya Pradesh'
       
    elif data=="Maharashtra":
        state_job=JobPost.objects.filter(state='Maharashtra').filter(is_verify=True)
        job_name='Maharashtra'
       
    elif data=="Manipur":
        state_job=JobPost.objects.filter(state='Manipur').filter(is_verify=True)
        job_name='Manipur'
    elif data=="Meghalaya":
        state_job=JobPost.objects.filter(state='Meghalaya').filter(is_verify=True)
        job_name='Meghalaya'
    elif data=="Mizoram":
        state_job=JobPost.objects.filter(state='Mizoram').filter(is_verify=True)
        job_name='Mizoram'
    elif data=="Nagaland":
        state_job=JobPost.objects.filter(state='Nagaland').filter(is_verify=True)
        job_name='Nagaland'
    elif data=="Odisha":
        state_job=JobPost.objects.filter(state='Odisha').filter(is_verify=True)
        job_name='Odisha'
    elif data=="Puducherry":
        state_job=JobPost.objects.filter(state='Puducherry').filter(is_verify=True)
        job_name='Puducherry'
    elif data=="Punjab":
        state_job=JobPost.objects.filter(state='Punjab').filter(is_verify=True)
        job_name='Punjab'
    elif data=="Rajasthan":
        state_job=JobPost.objects.filter(state='Rajasthan').filter(is_verify=True)
        job_name='Rajasthan'
    elif data=="Sikkim":
        state_job=JobPost.objects.filter(state='Sikkim').filter(is_verify=True)
        job_name='Sikkim'
    elif data=="Tamil_Nadu":
        state_job=JobPost.objects.filter(state='Tamil_Nadu').filter(is_verify=True)
        job_name='Tamil Nadu'
    elif data=="Telangana":
        state_job=JobPost.objects.filter(state='Telangana').filter(is_verify=True)
        job_name='Telangana'
    elif data=="Tripura":
        state_job=JobPost.objects.filter(state='Tripura').filter(is_verify=True)
        job_name='Tripura'
    elif data=="Uttarakhand":
        state_job=JobPost.objects.filter(state='Uttarakhand').filter(is_verify=True)
        job_name='Uttarakhand'
    elif data=="Uttar Pradesh":
        state_job=JobPost.objects.filter(state='Uttar_Pradesh').filter(is_verify=True)
        job_name='Uttar Pradesh'
    elif data=="West_Bengal":
        state_job=JobPost.objects.filter(state='West_Bengal').filter(is_verify=True)
        job_name='West Bengal'
    elif data=="All_India":
        state_job=JobPost.objects.all().filter(is_verify=True)
        job_name='All India'
    print(data)
    print(state_job)
    
  
    return render(request,'state_job.html',{'state_job':state_job,'job_name':job_name,}) 
        

class JobDetailView(View):
	def get(self, request, pk):
		
		job_details =JobPost.objects.get(pk=pk)	
			
		return render(request, 'jobdetail.html', {'job_detail_page':job_details, })


def jobNatificationsMail(request):
    
    return render(request,'index.html')




