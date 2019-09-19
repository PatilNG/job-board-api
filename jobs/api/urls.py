from django.urls import path
from jobs.api.views import JobOfferListCraeteAPIView, JobOfferDetailAPIView

urlpatterns=[

    path("jobs/", JobOfferListCraeteAPIView.as_view(), name = "job-list"),
    path("jobs/<int:pk>", JobOfferDetailAPIView.as_view(), name = "job-details")
]
