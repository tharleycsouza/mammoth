
from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class BarmanConfig(AppConfig):
    name = 'barman'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
