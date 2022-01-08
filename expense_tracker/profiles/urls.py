from django.urls import path

from expense_tracker.profiles.views import profile_detail, create_profile, profile_edit, profile_delete

urlpatterns = (
    path('', profile_detail, name='profile detail'),
    path('create/', create_profile, name='create profile'),
    path('edit/', profile_edit, name='edit profile'),
    path('delete/', profile_delete, name='delete profile'),
)
