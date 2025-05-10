from app.repository.advertiser_repository import AdvertiserRepository

class AdvertiserService():
    def __init__(self, advertiser_repository: AdvertiserRepository):
        self.advertiser_repository = advertiser_repository
    
    def get_all(self):
        return self.advertiser_repository.get_all()