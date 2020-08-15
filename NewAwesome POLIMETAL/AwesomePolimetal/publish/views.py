from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.views.generic import ( TemplateView,
																	ListView, 
																	DetailView, 
																	CreateView,
																	UpdateView,
																	DeleteView, )
from .models import Company, Category, Advert, AdvertCategory
from .forms import CompanyForm, CompanyUpdateForm, AdvertForm, AdvertUpdateForm


def home(request):
		return render (request, "index.html")

def about(request):
		return render (request, "about.html")



#LEGAL

def privacypolicy(request):
		return render (request, "privacy_policy.html")

def termsofuse(request):
		return render (request, "terms_of_use.html")



#CALCULATORS

def units(request):
		return render (request, "units.html")

def meterstons(request):
		return render (request, "meters_tons.html")		

def es_valor_cu(request):
		return render (request, "es_valor_cu.html")	

def es_valor_pb_zn(request):
		return render (request, "es_valor_pb_zn.html")	

def es_valor_au(request):
		return render (request, "es_valor_au.html")	




#CATEGORYS for Company

def CategoryView(request, cats):
		CategoryCompanys = Company.objects.filter(category=cats).order_by('-date_posted')
		return render (request, "categories.html", {"cats": cats.title(),"CategoryCompanys": CategoryCompanys})

#COMPANYS
class CompanyListView(ListView):
		model = Company
		template_name = "company_list.html"
		context_object_name = 'companys'
		ordering = ["-date_posted"]
		paginate_by = 1


class CompanyDetailView(DetailView):
		model = Company
		template_name = "company_detail.html"
		context_object_name = 'companys-detail'


class CompanyCreateView(LoginRequiredMixin,CreateView):
		model = Company
		form_class = CompanyForm
		template_name = "company_form.html"
		context_object_name = 'company-create'


		def form_valid(self, form):
				form.instance.author = self.request.user	
				return super().form_valid(form)			


class CompanyUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
		model = Company
		template_name = "company_form.html"
		context_object_name = 'company-update'
		form_class = CompanyUpdateForm

		def form_valid(self, form):
				form.instance.author = self.request.user	
				return super().form_valid(form)		

		def test_func(self):
				company = self.get_object()
				if self.request.user == company.author:
						return True
				return False

class CompanyDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
		model = Company
		template_name = "company_delete.html"
		context_object_name = 'company-delete'
		success_url = "/"

		def test_func(self):
				company = self.get_object()
				if self.request.user == company.author:
						return True
				return False



# ADVERTISING
#CATEGORYS for Advert

def AdvertCategoryView(request, cats):
		AdvertCategory = Advert.objects.filter(category=cats).order_by('-date_posted')
		return render (request, "advert_categories.html", {"cats": cats.title(),"AdvertCategory": AdvertCategory})

class AdvertListView(ListView):
		model = Advert
		template_name = "advert_list.html"
		context_object_name = 'adverts'
		ordering = ["-date_posted"]
		paginate_by = 2


class AdvertDetailView(DetailView):
		model = Advert
		template_name = "advert_detail.html"
		context_object_name = 'advert-detail'


class AdvertCreateView(LoginRequiredMixin,CreateView):
		model = Advert
		form_class = AdvertForm
		template_name = "advert_form.html"
		context_object_name = 'advert-create'
		ordering = ["name"]


		def form_valid(self, form):
				form.instance.author = self.request.user	
				return super().form_valid(form)			


class AdvertUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
		model = Advert
		template_name = "advert_form.html"
		context_object_name = 'advert-update'
		form_class = AdvertUpdateForm

		def form_valid(self, form):
				form.instance.author = self.request.user	
				return super().form_valid(form)		

		def test_func(self):
				advert = self.get_object()
				if self.request.user == advert.author:
						return True
				return False

class AdvertDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
		model = Advert
		template_name = "advert_delete.html"
		context_object_name = 'advert-delete'
		success_url = "/"

		def test_func(self):
				advert = self.get_object()
				if self.request.user == advert.author:
						return True
				return False

