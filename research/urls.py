from django.urls import path

from .views import (
    StartResearch,
    ContinueResearch,
    UploadDocument,
    ResearchHistory,
    ResearchDetails,
)

urlpatterns = [
    
    path("start/", StartResearch.as_view()),
    path("<int:research_id>/continue/", ContinueResearch.as_view()),
    path("<int:research_id>/upload/", UploadDocument.as_view()),
    path("history/", ResearchHistory.as_view()),
    path("<int:research_id>/", ResearchDetails.as_view()),
]
