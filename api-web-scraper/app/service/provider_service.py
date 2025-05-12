from app.repository.provider_repository import ProviderRepository

class ProviderService():
    def __init__(self, provider_repository: ProviderRepository):
        self.provider_repository = provider_repository
    
    def get_all(self):
        return self.provider_repository.get_all()