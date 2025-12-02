from pytest_query.fixtures import (
    services_inventory,
    service_mangers,
    service_queries,
    service_sessions,
)


def pytest_addoption(parser):
    """Add options to control pytest-queries."""
    group = parser.getgroup("pytest-queries")
    group.addoption(
        "--service-inventory",
        action="store",
        dest="service_inventory",
        default="",
        help="Configure the service inventory path",
    )
