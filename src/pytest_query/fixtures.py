#
# 1、获取所有的管理器
# 2、获取querys和session
import os
import pytest as pytest
import yaml

from pytest_query.core.inventory import ServicesInventory
from pytest_query.core.registry import service_manger, service_query, service_session


@pytest.fixture(scope="session")
def services_inventory(request):
    file_path = request.config.getoption("service_inventory")
    # file_path = os.path.join(request.config.getoption("rootdir"), file_path)
    inventory = ServicesInventory.new_from_file(file_path)
    return inventory


@pytest.fixture(scope="session")
def service_mangers(services_inventory):
    def get_query_manger(name):
        return service_manger.get(name)(inventory=services_inventory)

    return get_query_manger


@pytest.fixture(scope="session")
def service_querys(services_inventory):
    def get_query_manger(name):
        return service_query.get(name)(services_inventory)

    return get_query_manger


@pytest.fixture(scope="session")
def service_sessions(services_inventory):
    def get_query_manger(name):
        return service_session.get(name)(services_inventory)

    return get_query_manger
