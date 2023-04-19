from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("chineseGPT/", views.chineseGPT, name="chineseGPT"),
    path("chineseGPT/translation/", views.translation_bot, name="translation"),
    path("user_reviews/", views.user_reviews, name='user_reviews'),
    path("about/", views.about, name="about"),
    path("AIGenerated_quiz/", views.generate_quiz, name='ai_quiz'),
    path("convo_simulation/", views.conversation_simulation, name="convo_simulation"),
    path("personalized_lessons/", views.personalized_lessons, name="personalized_lessons"),
    path("gamification/", views.gamefication, name="gamification")
]