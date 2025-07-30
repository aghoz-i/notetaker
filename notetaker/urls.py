from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from notes.views import NoteListView, NoteDetailView

urlpatterns = [
    path('api/v1/notes/', NoteListView.as_view(), name='note-list'),
    path('api/v1/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('api/v1/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]