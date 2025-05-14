from app.repository.advertiser_repository import AdvertiserRepository
from app.dependencies.advertiser_filters import AdvertiserFilters
from app.dependencies.pagination_params import PaginationParams


class AdvertiserService():
    def __init__(self, advertiser_repository: AdvertiserRepository):
        self.advertiser_repository = advertiser_repository
    
    def get_all(self):
        return self.advertiser_repository.get_all()
    
    def get_advertiser(self, filters: AdvertiserFilters, pagination: PaginationParams):
        return self.advertiser_repository.get_advertiser(filters, pagination)