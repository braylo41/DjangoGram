from django.urls import path
from .views import SignUpView, CustomUserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(), name='update')
]
