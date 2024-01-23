from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views import View
# Create your views here.

class CreateRoomView(View):
    def get(self, request):
        form = CreateRoom()
        return render(request, 'create_chat.html', {'form': form})


    def post(self, request):
        if request.user.is_authenticated:
            if request.POST.get('reason_title') == "" or request.POST.get('reason_title') == None:
                return render(request, 'create_chat.html', {'error': True})
            form = CreateRoom(request.POST)
            if form.is_valid():
                chat = form.save(commit=False)
                chat.author = request.user
                chat.save()
                
                chat.listUsers.add(request.user)
                chat.save()

                return redirect('support_chat', pk=chat.pk)
            else:
                form = CreateRoom()
        else:
            return redirect('register')
        return render(request, 'create_chat.html', {'form': form})
    
def ChatRoomDetailView(request, pk):
    if request.user.is_authenticated:
        try:
            listdetail = SupportModel.objects.get(pk=pk)
        except SupportModel.DoesNotExist:
            return HttpResponse("Object doesn't exist", status=404)
    else:
        return redirect('home')
    
    listUsersNames = [user.username for user in listdetail.listUsers.all()]
    listUsersId = listdetail.listUsers.all()

    new_participant = request.user

    for user_channl in listUsersId:
        if user_channl != new_participant:
            chat = get_object_or_404(SupportModel, pk=pk)
            chat.listUsers.add(new_participant)
            chat.save

    chat = get_object_or_404(SupportModel, pk=pk)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            sender = request.user
            message = MessageModel.objects.create(chat=chat, sender=sender, content=content)

            return redirect('support_chat', pk=pk)
    else:
        form = SendMessageForm()

    messages = MessageModel.objects.filter(chat__pk=pk)

    if request.method == 'POST':
        listdetail.status = True
        listdetail.save()
        return redirect('support_list')

    return render(request, 'chat_room.html', {'form': form, 'messages': messages ,'listdetail': listdetail, 'listUsers': listUsersNames})

    
class ChatListView(UserPassesTestMixin, View):
    def get(self, request):
        uncompleted = SupportModel.objects.filter(status=False).order_by('-pk')
        return render(request, 'list_of_chats.html', {'uncompleted': uncompleted})
    
    def test_func(self):
        return self.request.user.is_staff

class UsersRequests(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            user_requests = SupportModel.objects.filter(author=user)
            return render(request, 'user_requests.html', {'user_requests': user_requests})
        else:
            return redirect('home')

class CompletedRequests(UserPassesTestMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            completed_requests = SupportModel.objects.filter(status=True).order_by('-pk')
            return render(request, 'completed_requests.html', {'completed_requests': completed_requests})
        else:
            return redirect('home')
        
    def test_func(self):
        return self.request.user.is_staff