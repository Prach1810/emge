from django.forms import ModelForm

from home.models import Contact,Post,Company

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('Industry','company_type','Brand','Locations','phone','email','website','selfie' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Brand'].widget.attrs.update({'class' :'input--style-5','type':'text','placeholder':'Brand name','style':'width: 100%;'})
        self.fields['Industry'].widget.attrs.update({'class' :'input--style-5','type':'text','style':'height:50px;width:500px;'})
        self.fields['company_type'].widget.attrs.update({'class' :'input--style-5','type':'text','style':'height:50px;width:500px;'})
        #self.fields['Locations'].widget.attrs.update({'class' :'input--style-5','type':'text','placeholder':'.....'})
        self.fields['phone'].widget.attrs.update({'class' :'input--style-5','type':'number','placeholder':'call','style':'width: 100%;'})
        self.fields['email'].widget.attrs.update({'class' :'input--style-5','type':'email','placeholder':'Your email..','style':'width: 100%;'})
        self.fields['website'].widget.attrs.update({'class' :'input--style-5','type':'text','placeholder':'Paste the link','style':'width: 100%;'})
        self.fields['selfie'].widget.attrs.update({'class' :'custom-file-input','type':'file',' id':'inputGroupFile'})
        self.fields['Locations'].widget.attrs.update({'class':'drop','type':'text','id':'txtdisplay' ,'style ':'font-family: inherit;width: 297px;','readonly name':'Locations'})



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','subject','mssg' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' :'form-control','type':'name','placeholder':'Your name'})
        self.fields['email'].widget.attrs.update({'class' :'form-control','type':'email','placeholder':'Your email..'})
        self.fields['subject'].widget.attrs.update({'class' :'form-control','type':'text','placeholder':'Subject'})
        self.fields['mssg'].widget.attrs.update({'class' :'form-control','type':'msg','placeholder':'Message'})
        
        
class Profile(ModelForm):
    class Meta:
        model = Company
        fields = ('name','organisation','email','Intro','document','contact','CIN','logo' ,'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        companies = Company.objects.get(id__exact=1)
        self.fields['name'].widget.attrs.update({'class' :'form-control','type':'text','name':'first_name'})
        self.fields['name'].initial = companies.name
        self.fields['email'].widget.attrs.update({'class' :'form-control','type':'email','name':'email'})
        self.fields['email'].initial = companies.email
        self.fields['password'].widget.attrs.update({'class' :'input--style-5','type':'password','name':'password'})
        self.fields['organisation'].widget.attrs.update({'class' :'input--style-5','type':'text','name':'company'})
        self.fields['Intro'].widget.attrs.update({'class' :'form-control','id':'exampleFormControlTextarea1', 'rows':'5 '})
        self.fields['Intro'].initial = companies.Intro
        self.fields['document'].widget.attrs.update({'class' :'custom-file-input','type':'file','id':'inputGroupFile'})
        self.fields['contact'].widget.attrs.update({'class' :'form-group','type':'text','name':'mobile','style':'width: 100%;'})
        self.fields['contact'].initial = companies.contact
        self.fields['logo'].widget.attrs.update({'class' :'custom-file-input','type':'file','id':'inputGroupFile'})