from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Group, Event
from .forms import EventForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard (request):
    return render(request, 'dashboard.html')

def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'groups': groups})

def groups_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    # events = Event.objects.get(id=group_id)
    event_form = EventForm()
    return render(request, 'groups/detail.html',{'group': group, 'event_form': event_form})

def events_detail(request, group_id, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html',{'event': event})

# Class-Based View (CBV)
class GroupCreate(LoginRequiredMixin, CreateView):
  model = Group
  fields = ['name', 'description']

  # This inherited method is called when a
  # valid group form is being submitted
  def form_valid(self, form):
    # form.instance is the group object
    form.instance.user = self.request.user
    return super().form_valid(form)

def add_event(request, group_id):
  #create a ModelForm instance using the data in request.POST
  form = EventForm(request.POST)
  #check if form is valid
  if form.is_valid():
    # don't want to try to save the feeding
    # until the cat_id has been assigned
    new_event = form.save(commit=False)
    new_event.group_id = group_id
    new_event.save()
  return redirect('detail', group_id=group_id)

def events_create(request, group_id):
  event_form = EventForm()
  return render(request, {'event_form': event_form})

# # Class-Based View (CBV)
class EventCreate(LoginRequiredMixin, CreateView):
  model = Event
  fields = ['title', 'host', 'location', 'datetime']

  # This inherited method is called when a
  # valid group form is being submitted
  def form_valid(self, form):
    form.instance.group = self.request.group
    # form.instance is the group object
    form.instance.user = self.request.user
    return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect ('dashboard')
    else:
      error_message = 'Invalid Sing Up, Try Again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

