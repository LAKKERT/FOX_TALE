from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import NewsContent
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
# Create your views here.

class NewsView(ListView):
    model = NewsContent
    template_name = 'news.html'
    ordering = ['-date_add']

# def is_staff(user):
#     return user.is_authenticated and user.is_staff

class NewsDetailView(View):

    def get(self, request, pk):
        try:
            newsDetail = NewsContent.objects.get(pk=pk)
        except NewsContent.DoesNotExist:
            return redirect('home')
        return render(request, 'new_detail.html', {'newsDetail': newsDetail})

    def post(self, request, pk):
        if request.method == 'POST':
            NewsContent.objects.filter(pk=pk).delete()
            return redirect('news')
    
class NewsCreateView(UserPassesTestMixin, CreateView):
    model = NewsContent
    form_class = NewsForm
    template_name = "add_news.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff

class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsContent
    form_class = NewsForm
    template_name = "new_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff
    
    def get_absolute_url(self):
        return reverse('new_update', kwargs={'pk': self.pk})