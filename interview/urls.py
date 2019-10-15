from django.urls import path, include
from .views import SlotView, AvailableList, InterviewView, SlotOptionView
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('slots', SlotView)
router.register('interviews', InterviewView)
router.register('slotoptions', SlotOptionView)

urlpatterns = [
    path("", include(router.urls)),
    url(r'^schedule/', AvailableList.as_view()),

]