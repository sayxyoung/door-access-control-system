from django.urls import path
from .views import CreateUserGenericView

urlpatterns = [
    path('/create', CreateUserGenericView.as_view(), name='create'),
]