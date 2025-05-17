from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from clientes.api import viewsets as clientesviewsets
from servicos.api import viewsets as servicosviewsets
from profissionais.api import viewsets as profissionaisviewsets
from agendamentos.api import viewsets as agendamentosviewsets

route = DefaultRouter()
route.register(r'clientes', clientesviewsets.ClientesViewsets, basename="Clientes")
route.register(r'servicos', servicosviewsets.ServicosViewSets, basename="Serviços")
route.register(r'profissionais', profissionaisviewsets.ProfissionaisViewSets, basename="Profissionais")
route.register(r'agendamentos', agendamentosviewsets.AgendamentosViewSets, basename="Agendamentos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]
