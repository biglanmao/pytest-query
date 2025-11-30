def pytest_addoption(parser):
    parser.addini("service_inventory", help="Configure the service inventory path")
