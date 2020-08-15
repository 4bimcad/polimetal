from django.contrib import admin  
from django.urls import path, include
from .views import (                    CompanyListView, 
									 	CompanyDetailView, 
										CompanyCreateView,
										CompanyUpdateView,
									 	CompanyDeleteView,
                                        CategoryView,
                                        
                                        AdvertListView, 
                                        AdvertDetailView, 
                                        AdvertCreateView,
                                        AdvertUpdateView,
                                        AdvertDeleteView,
                                        AdvertCategoryView,
                                       
									 )
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('privacy-policy/', views.privacypolicy, name="privacy-policy"),
    path('terms-of-use/', views.termsofuse, name="terms-of-use"),
    path('tools/units/', views.units, name="units"),
    path('tools/meters-tons/', views.meterstons, name="meters-tons"),
    path('tools/es-valor-cu/', views.es_valor_cu, name="es-valor-cu"),
    path('tools/es-valor-pb-zn/', views.es_valor_pb_zn, name="es-valor-pb-zn"),
    path('tools/es-valor-au/', views.es_valor_au, name="es-valor-au"),


  	path('company/list/', CompanyListView.as_view(), name="company-list"),
    path('company/new/', CompanyCreateView.as_view(), name="company-create"),
    path('company/<int:pk>/update', CompanyUpdateView.as_view(), name="company-update"),
    path('company/<int:pk>/delete', CompanyDeleteView.as_view(), name="company-delete"),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name="company-detail"),
    path('category/<str:cats>/', CategoryView, name="category"), 

    path('advert/list/', AdvertListView.as_view(), name="advert-list"),
    path('advert/new/', AdvertCreateView.as_view(), name="advert-create"),
    path('advert/<int:pk>/update', AdvertUpdateView.as_view(), name="advert-update"),
    path('advert/<int:pk>/delete', AdvertDeleteView.as_view(), name="advert-delete"),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name="advert-detail"),
    path('advert/<str:cats>/', AdvertCategoryView, name="advert-category"), 
]
