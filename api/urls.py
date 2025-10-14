from django.urls import path
from . import views

urlpatterns = [
    path('process-cv/', views.process_cv_view, name='process_cv'),
    # path('generate-docx/', views.generate_docx_view, name='generate_docx'),
]