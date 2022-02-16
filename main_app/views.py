from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Group, Event, Profile, User, Recipe
from .forms import EventForm, ProfileForm, RecipeForm

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
    group = Group.objects.get(id=group_id)
    event = Event.objects.get(id=event_id)
    recipes = Recipe.objects.filter(user=request.user)

    id_list = recipes.event.all().values_list('id')
    print(id_list)
    # recipes_in_event = Recipe.objects.exclude(id__in=id_list)
    # recipes_notin_event = Toy.objects.exclude(id__in=id_list)
    return render(request, 'events/detail.html', {'event': event, 'recipes': recipes, "group": group})

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
  return render(request, {'event_form': event_form}, group_id=group_id)

# # Class-Based View (CBV)
# class EventCreate(LoginRequiredMixin, CreateView):
#   model = Event
#   fields = ['title', 'host', 'location', 'datetime']

#   # This inherited method is called when a
#   # valid group form is being submitted
#   def form_valid(self, form):
#     # form.instance is the group object
#     form.instance.user = self.request.user
#     return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect ('profile_form')
    else:
      error_message = 'Invalid Sign Up, Try Again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def profile_form(request):
  profile_form = ProfileForm()
  return render(request, 'registration/profile_form.html', {'profile_form': profile_form})

def add_profile(request):
  current_user = request.user
  #create a ModelForm instance using the data in request.POST
  form = ProfileForm(request.POST)
  #check if form is valid
  if form.is_valid():
    new_profile = form.save(commit=False)
    new_profile.user = current_user
    new_profile.save()
  return redirect('dashboard')

# Class-Based View (CBV)
class GroupCreate(LoginRequiredMixin, CreateView):
  model = Group
  fields = ['name', 'description']

  # This inherited method is called when a
  # valid group form is being submitted
  def form_valid(self, form):
    # form.instance is the group object
    form.instance.user = self.request.user
    form.instance.leader = self.request.user.username
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
  return render(request, {'event_form': event_form}, group_id=group_id)

# # Class-Based View (CBV)
# class EventCreate(LoginRequiredMixin, CreateView):
#   model = Event
#   fields = ['title', 'host', 'location', 'datetime']

#   # This inherited method is called when a
#   # valid group form is being submitted
#   def form_valid(self, form):
#     # form.instance is the group object
#     form.instance.user = self.request.user
#     return super().form_valid(form)

@login_required
def assoc_profile(request, group_id):
  profile_id = Profile.objects.get(user=request.user)
  group = Group.objects.get(id=group_id)
  group.members.add(profile_id)
  return redirect('detail', group_id=group_id)

@login_required
def unassoc_profile(request, group_id):
  profile_id = Profile.objects.get(user=request.user)
  group = Group.objects.get(id=group_id)
  group.members.remove(profile_id)
  return redirect('detail', group_id=group_id)

def recipes_index(request):
  recipe_form = RecipeForm()
  recipes = Recipe.objects.filter(user=request.user)
  return render(request, 'recipes/index.html', {
    'recipe_form': recipe_form, 
    'recipes': recipes
  })

def add_recipe(request):
  #create a ModelForm instance using the data in request.POST
  form = RecipeForm(request.POST)
  print('adele says hello')
  #check if form is valid
  if form.is_valid():
    # don't want to try to save the feeding
    # until the cat_id has been assigned
    new_recipe = form.save(commit=False)
    new_recipe.user = request.user
    new_recipe.save()
    print('hello')
  return redirect('recipes_index')

@login_required
def assoc_recipe(request, group_id, event_id):
  recipe_id = request.POST['recipes']
  print(recipe_id)
  recipe = Recipe.objects.get(id=recipe_id)
  recipe.events.add(event_id)
  return redirect('events_detail', group_id, event_id)

