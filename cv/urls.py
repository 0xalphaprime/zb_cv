from django.urls import path


from . import views

app_name = "cv"

urlpatterns = [
    path("", views.cv, name="cv"),
    path("slb/", views.slb, name="zbslb"),
    path("ez/", views.ez, name="zbez"),
    path("sl360/", views.sl360, name="zbsl360"),
    path("xp/", views.xp, name="zbxp"),
    path("wires_and_cables/", views.wires_and_cables, name="zbwires"),
]
