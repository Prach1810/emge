from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from .models import Company, Contact,Post 
from home.forms import ContactForm,Profile,PostForm 
from EMGE.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    else:
        return redirect(reverse('login'))

def partner(request):
	if request.method == 'POST':
		form2 = ContactForm(request.POST, request.FILES or None)
		print(form2.errors)
		if form2.is_valid():
			
			form2.save()
			#return redirect('partner')
			subject= form2.cleaned_data.get('subject')
			message=form2.cleaned_data.get('mssg')
			recepient=form2.cleaned_data.get('email')
			send_mail(subject, 
				message, recepient, [ EMAIL_HOST_USER], fail_silently = False)	
			return render(request, 'home/success.html', {'recepient': recepient})
	else:
		form2 = ContactForm()

	context = {'form2' : form2}
	return render(request,'home/partner.html',context)

def about(request):
    return render(request,'home/aboutus.html')

"""
def companyprofile(request,k):
	companies = Company.objects.all()
	search_term=''

	if 'name' in request.GET:
		companies = companies.order_by('id')
	
	
	if 'search' in request.GET:
		if(k==0):
		
			search_term= request.GET['search']
			companies = companies.filter(name__icontains=search_term)
		
		if k==1:
			
			search_term= request.GET['search']
			companies = companies.filter(Locations__icontains=search_term)
	

	context = {'companies' : companies,'search_term' : search_term}
	return render(request,'home/company_profile.html', context)
"""

def dashboard(request):
    return render(request,'home/dashboard1.html')

def terms(request):
    return render(request,'home/terms.html')

def profile(request):
	#info = Post.objects.filter(id=inf_id)
	companies = Company.objects.get(id__exact=1)
	print()
	
	
	if request.method == 'POST':
		form3 = Profile(request.POST, request.FILES or None )
		print(form3.errors)
		
		if form3.is_valid():
			
			form3.save()
			return redirect('home')
	else:
		form3 = Profile()

	context = {'media_url':settings.MEDIA_URL,'form3':form3,'companies':companies}
	
	return render(request,'home/profile.html', context)

def search(request):

	posts = Post.objects.all()
	companies = Company.objects.all()
	#foo=request.GET.get('foo')
	foo = request.GET.get('bar')
	print(foo)
	
	search_term=''

	if 'name' in request.GET:
		posts = posts.order_by('id')
	
	if 'search' in request.GET:
		search_term= request.GET['search']
		mylist = search_term.split(',')
		c=len(mylist)
		k=0
		group=[]
		res=[]

		for j in mylist:
			if k<c:
			#posts = posts.filter(Locations__icontains=i)			
				group.append(posts.filter(Locations__icontains=j))
				k+=1
				
		#companies=companies.filter(id == posts.industry)
	res = list(set(i for j in group for i in j))
	
	context = {'res' : res,'media_url':settings.MEDIA_URL,'companies':companies}
	return render(request, 'home/search1.html', context)


def companyprofile(request, inf_id):
	info = Post.objects.filter(id=inf_id)
	#companies = Company.objects.all()
	context = {'info' : info}
	"""
	search_term=''

	if 'name' in request.GET:
		posts = posts.order_by('id')
	
	
	if 'search' in request.GET:
		search_term= request.GET['search']
		posts = posts.filter(Locations__icontains=search_term)
		#companies=companies.filter(id == posts.industry)
	
	context = {'posts' : posts,'search_term' : search_term,'media_url':settings.MEDIA_URL,'companies':companies}
	"""
	return render(request,'home/company_profile.html', context)

def post(request):
	
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES or None)
		print(form.errors)
		if form.is_valid():
			
			form.save()
			return redirect('home')
	else:
		form = PostForm()

	context = {'form' : form}
	return render(request,'home/contactform.html',context)