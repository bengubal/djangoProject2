from django.urls import path
from .views import homePageView
from .views import HomePageView
from .views import HomePageView, AboutPageView



urlpatterns = [
  #  path("", homePageView, name="home"),
    path("", HomePageView.as_view(), name="homepage"),
    path("about/", AboutPageView.as_view(), name="about"),
]
