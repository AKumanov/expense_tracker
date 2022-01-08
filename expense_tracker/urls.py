from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expense_tracker.expenses.urls')),
    path('profile/', include('expense_tracker.profiles.urls'))
]
