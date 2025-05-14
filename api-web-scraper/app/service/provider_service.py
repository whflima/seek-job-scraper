from app.repository.provider_repository import ProviderRepository
from app.dependencies.provider_filters import ProviderFilters
from app.dependencies.pagination_params import PaginationParams

class ProviderService():
    def __init__(self, provider_repository: ProviderRepository):
        self.provider_repository = provider_repository
    
    def get_all(self):
        return self.provider_repository.get_all()
    
    def get_provider(self, filters: ProviderFilters, pagination: PaginationParams):
        return self.provider_repository.get_provider(filters, pagination)