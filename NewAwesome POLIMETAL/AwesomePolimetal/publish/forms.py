from django import forms
from .models import Company, Category, Advert, AdvertCategory


# CHOICES for Categorys

choices = Category.objects.all().values_list('title','title')
choice_list = []

for item in choices:
		choice_list.append(item)



class CompanyForm(forms.ModelForm):
	
		class Meta:
				model = Company
				fields = ("name", 
									"category",
									"breve", 
									"description", 
									"email", 
									"website", 
									"phone",
									"location", 									
					)
				widgets = { 
									"name": forms.TextInput(attrs={"class":"form-control"}),
									"category": forms.Select(choices=choice_list,attrs={"class":"form-control"}),
									"breve": forms.TextInput(attrs={"class":"form-control"}),
									"description": forms.Textarea(attrs={"class":"form-control"}),
									"email": forms.TextInput(attrs={"class":"form-control"}),
									"website": forms.TextInput(attrs={"class":"form-control"}),
									"phone": forms.TextInput(attrs={"class":"form-control"}),
									"location": forms.Select(attrs={"class":"form-control"}),
				}



class CompanyUpdateForm(forms.ModelForm):
		class Meta:
				model = Company
				fields = ("name", 
									"category",
									"breve", 
									"description", 
									"email", 
									"website", 
									"phone",
									"location", 									
					)
				widgets = { 
									"name": forms.TextInput(attrs={"class":"form-control"}),
									"category": forms.Select(choices=choice_list,attrs={"class":"form-control"}),
									"breve": forms.TextInput(attrs={"class":"form-control"}),
									"description": forms.Textarea(attrs={"class":"form-control"}),
									"email": forms.TextInput(attrs={"class":"form-control"}),
									"website": forms.TextInput(attrs={"class":"form-control"}),
									"phone": forms.TextInput(attrs={"class":"form-control"}),
									"location": forms.Select(attrs={"class":"form-control"}),
				}


#ADVERTISING

# CHOICES for ADVERTS
advert_choices = AdvertCategory.objects.all().values_list('title','title')
advert_choice_list = []

for item in advert_choices:
		advert_choice_list.append(item)



class AdvertForm(forms.ModelForm):
		class Meta:
				model = Advert
				fields = ("name", 
									"category",
									"breve", 
									"description", 
									"email", 
									"website", 
									"phone",
									"location", 									
					)
				widgets = { 
									"name": forms.TextInput(attrs={"class":"form-control"}),
									"category": forms.Select(choices=advert_choice_list,attrs={"class":"form-control"}),
									"breve": forms.TextInput(attrs={"class":"form-control"}),
									"description": forms.Textarea(attrs={"class":"form-control"}),
									"email": forms.TextInput(attrs={"class":"form-control"}),
									"website": forms.TextInput(attrs={"class":"form-control"}),
									"phone": forms.TextInput(attrs={"class":"form-control"}),
									"location": forms.Select(attrs={"class":"form-control"}),
				}


class AdvertUpdateForm(forms.ModelForm):
		class Meta:
				model = Advert
				fields = ("name", 
									"category",
									"breve", 
									"description", 
									"email", 
									"website", 
									"phone",
									"location", 									
					)
				widgets = { 
									"name": forms.TextInput(attrs={"class":"form-control"}),
									"category": forms.Select(choices=advert_choice_list,attrs={"class":"form-control"}),
									"breve": forms.TextInput(attrs={"class":"form-control"}),
									"description": forms.Textarea(attrs={"class":"form-control"}),
									"email": forms.TextInput(attrs={"class":"form-control"}),
									"website": forms.TextInput(attrs={"class":"form-control"}),
									"phone": forms.TextInput(attrs={"class":"form-control"}),
									"location": forms.Select(attrs={"class":"form-control"}),
				}


