from pytest_querys.fixtures import (
    services_inventory,
    service_mangers,
    service_querys,
    service_sessions,
)


def pytest_addoption(parser):
    """Add options to control pytest-querys."""
    group = parser.getgroup("pytest-querys")
    group.addoption(
        "--service-inventory",
        action="store",
        dest="service_inventory",
        default="",
        help="Configure the service inventory path",
    )
