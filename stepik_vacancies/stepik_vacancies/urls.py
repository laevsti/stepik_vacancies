from django.urls import path
from vacancies.views import MainView, ListVacanciesView, VacancyView, VacanciesSpecListView, CompanyView
from vacancies.views import custom_handler400, custom_handler403, custom_handler404, custom_handler500


urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('vacancies', ListVacanciesView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:category>', VacanciesSpecListView.as_view(), name='spec_vacancies'),
    path('companies/<int:comp_num>', CompanyView.as_view(), name='company'),
    path('vacancies/<int:pk>', VacancyView.as_view(), name='vacancy'),
]

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500
