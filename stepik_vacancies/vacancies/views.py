from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from django.db.models import Count
from django.views.generic import ListView, TemplateView, DetailView

from vacancies.models import Company, Vacancy, Specialty


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        speciality = Specialty.objects.annotate(vac_count=Count('vacancies'))
        companies = Company.objects.annotate(vac_count=Count('vacancies'))
        context['specialties_list'] = speciality
        context['companies_list'] = companies
        return context


class VacanciesSpecListView(ListView):
    template_name = 'vacancies.html'
    model = Vacancy

    def get_queryset(self):
        return super().get_queryset().filter(specialty__code=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spec_list'] = Specialty.objects.filter(code=self.kwargs['category'])\
            .annotate(vac_count=Count('vacancies'))
        return context


class ListVacanciesView(ListView):
    template_name = 'vacancies.html'

    queryset = Vacancy.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        speciality = Specialty.objects.filter(pk__in=Vacancy.objects.values('specialty_id').distinct())\
            .annotate(vac_count=Count('vacancies'))
        context['spec_list'] = speciality
        return context


class VacancyView(DetailView):
    template_name = 'vacancy.html'

    model = Vacancy
    context_object_name = 'vacancy'


class CompanyView(ListView):
    template_name = 'company.html'

    context_object_name = 'company'
    model = Vacancy

    def get_queryset(self):
        return super().get_queryset().filter(company__id=self.kwargs['comp_num'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comp_details'] = Company.objects.get(pk=self.kwargs['comp_num'])
        context['vac_count'] = Vacancy.objects.filter(company__id=self.kwargs['comp_num']).count
        return context


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
