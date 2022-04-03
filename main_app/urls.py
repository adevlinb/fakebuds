
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile_form, name='profile_form'),
    path('accounts/profile/add/', views.add_profile, name='add_profile'),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('groups/', views.groups_index, name='index'),
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='groups_update'),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='groups_delete'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:group_id>/', views.groups_detail, name='detail'),
    # path('groups/<int:group_id>/add_photo_group', views.add_photo_group, name='add_photo_group'),
    path('groups/<int:group_id>/assoc_profile/', views.assoc_profile, name='assoc_profile'),
    path('groups/<int:group_id>/unassoc_profile/', views.unassoc_profile, name='unassoc_profile'),

    path('events/<int:group_id>/events_create/', views.events_create, name='events_create'),
    
    path('groups/<int:group_id>/add_event/', views.add_event, name='add_event'),
    path('events/<int:event_id>', views.events_detail, name='events_detail'),
    # path('events/<int:event_id>/add_photo_event', views.add_photo_event, name='add_photo_event'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/recipes_create_page', views.recipes_create_page, name="recipes_create_page"),
    path('recipes/add_recipe/', views.add_recipe, name='add_recipe'),
    # path('recipes/<int:recipe_id>/add_photo_recipe', views.add_photo_recipe, name='add_photo_recipe'),
    path('events/<int:event_id>/recipe/', views.assoc_recipe, name='assoc_recipe'),
    path('events/<int:event_id>/recipes/<int:recipe_id>/vote_up/', views.vote_up, name='vote_up'),
]