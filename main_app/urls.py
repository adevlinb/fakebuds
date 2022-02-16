
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile_form, name='profile_form'),
    path('accounts/profile/add/', views.add_profile, name='add_profile'),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('groups/', views.groups_index, name='index'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:group_id>/', views.groups_detail, name='detail'),
    path('groups/<int:group_id>/assoc_profile/', views.assoc_profile, name='assoc_profile'),
    path('groups/<int:group_id>/unassoc_profile/', views.unassoc_profile, name='unassoc_profile'),
    path('events/<int:group_id>/create/', views.events_create, name='events_create'),
    path('groups/<int:group_id>/add_event/', views.add_event, name='add_event'),
    path('groups/<int:group_id>/events/<int:event_id>', views.events_detail, name='events_detail'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/add_recipe/', views.add_recipe, name='add_recipe'),
    path('groups/<int:group_id>/events/<int:event_id>/recipe/', views.assoc_recipe, name='assoc_recipe')

]