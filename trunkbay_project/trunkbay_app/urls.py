from django.urls import path
from .views import *

urlpatterns = [
	# path('', home, name='home'),
	path('', home_proj, name='home_proj'),
]