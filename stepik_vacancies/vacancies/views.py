from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from django.db.models import Count

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
#        spec_name =
         return super().get_queryset().filter(specialty__code=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vac_count'] = Vacancy.objects.filter(specialty__code=self.kwargs['category']).count()
        context['spec_list'] = Specialty.objects.filter(code=self.kwargs['category'])
        return context


class ListVacanciesView(ListView):
    template_name = 'vacancies.html'

    queryset = Vacancy.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spec_list'] = Specialty.objects.all()
        context['vac_count'] = Vacancy.objects.all().count()
        return context

class VacancyView(View):
    def get(self, request, *args, **kwargs):

        content = {'title': 'title'
                   }
        return render(request, 'vacancy.html', {'content': content})

class CompanyView(View):
    def get(self, request, *args, **kwargs):

        content = {'title': 'title'
                   }
        return render(request, 'company.html', {'content': content})

