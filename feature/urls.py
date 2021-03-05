from django.urls import path
from feature.api import views as feature_api_views
urlpatterns = [
    path('features/', feature_api_views.FeatureList.as_view()),
]