from django.forms import SlugField
from django.http import request
from django.shortcuts import render
from django.urls import reverse
from .models import Movie, Genre, UpcomingMovie
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name = 'mainapp/base.html'
    context_object_name = 'movies'

    def get_queryset(self, *args, **kwargs):
        qs = super(MovieListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by('-pk')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming'] = UpcomingMovie.objects.all().order_by('-pk')
        return context

class MovieDetailView(LoginRequiredMixin,DetailView):
    model = Movie
    template_name = 'mainapp/movie-details.html'
    context_object_name = 'movie'
    login_url = '/account/login/'
    
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['genres'] = Genre.objects.filter(movie=super().get_object())
        context['othermovies'] = Movie.objects.all().order_by('-pk')
        context['upcoming'] = UpcomingMovie.objects.all().order_by('-pk')
        return context

    
class UpcomingDetailView(DetailView):
    model = UpcomingMovie
    template_name = 'mainapp/upcoming-details.html'
    context_object_name = 'upcoming'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['genres'] = Genre.objects.filter(upcomingmovie=super().get_object())
        context['movies'] = Movie.objects.all().order_by('-pk')
        context['otherupcoming'] = UpcomingMovie.objects.all().order_by('-pk')
        return context


class AboutView(TemplateView):
    template_name = 'mainapp/about-us.html'

class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'

class FaqView(TemplateView):
    template_name = 'mainapp/faq.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'mainapp/privacy-policy.html'