from enum import Enum, unique

from pytest_query.core.category import ServiceCategoryManager


@unique
class ServiceCategory(Enum):
    REDIS = "redis_server"
    WEB = "http_api_server"
    POSTGRES = "postgres_server"


ServiceCategoryManager.register_enum(ServiceCategory)
