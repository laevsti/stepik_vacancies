from django.urls import path
from vacancies.views import MainView, ListVacanciesView, VacancyView, VacanciesSpecListView, CompanyView


urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies', ListVacanciesView.as_view()),
    path('vacancies/cat/<str:category>', VacanciesSpecListView.as_view()),
    path('companies/<int:comp_num>', CompanyView.as_view()),
    path('vacancies/<int:vac_num>', VacancyView.as_view()),
]
