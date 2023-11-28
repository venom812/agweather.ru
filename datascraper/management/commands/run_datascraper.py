from django.core.management.base import BaseCommand
from datascraper.models import ForecastTemplate, ArchiveTemplate


class Command(BaseCommand):
    help = 'Run forecast scraper for forecast and archive.'

    def handle(self, *args, **kwargs):

        ForecastTemplate.scrap_forecasts()
        ArchiveTemplate.scrap_archives()