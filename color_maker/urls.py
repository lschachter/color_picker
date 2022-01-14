from django.urls import path

from color_maker.views import ColorPickerView


urlpatterns = [
    path('color-picker/', ColorPickerView.as_view()),
]