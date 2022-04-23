from django.core.management.base import BaseCommand

from vacancies.models import Company, Vacancy, Specialty
from vacancies.data import companies, jobs, specialties


class Command(BaseCommand):
    def handle(self, *args, **options):
        Company.objects.all().delete()
        Vacancy.objects.all().delete()
        Specialty.objects.all().delete()

        for i in companies:
            company = Company.objects.create(
                name=i['title'],
                location=i['location'],
                logo='https://place-hold.it/100x60',
                description=i['description'],
                employee_count=i['employee_count'],
            )

        for i in specialties:
            specialty = Specialty.objects.create(
                code=i['code'],
                title=i['title'],
            )

        for i in jobs:
            vacancy = Vacancy.objects.create(
                title=i['title'],
                specialty=Specialty.objects.get(code=i['specialty']),
                company=Company.objects.get(id=i['company']),
                skills=i['skills'],
                description=i['description'],
                salary_min=i['salary_from'],
                salary_max=i['salary_to'],
                published_at=i['posted'],
            )


