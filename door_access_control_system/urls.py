from django.urls import path, include

urlpatterns = [
    path('accounts', include('accounts.urls')),
    path('', include('accesses.urls')),
    path('api', include('accesses.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
