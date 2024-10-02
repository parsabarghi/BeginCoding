from . import views 
from django.urls import path



urlpatterns = [
    path('notes/', views.CreateNoteView.as_view(), name="Note-List"), 
    path('note/<int:pk>/edit/',views.NoteUpdate.as_view(), name='Note-Update'),
    path('note/delete/<int:pk>/', views.NoteDelete.as_view(), name='Note-Delete')
]
