from dependency_injector import containers, providers

from app.core.configs import configs
from app.core.database import Database
from app.repository import *
from app.service import *

class  Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.endpoints.advertiser",
            "app.api.endpoints.provider",
            "app.api.endpoints.job",
            "app.api.endpoints.stack"
        ]
    )
    
    db = providers.Singleton(Database, db_url=configs.DATABASE_URL)
    
    advertiser_repository = providers.Factory(AdvertiserRepository, session_factory=db.provided.session)
    provider_repository = providers.Factory(ProviderRepository, session_factory=db.provided.session)
    job_repository = providers.Factory(JobRepository, session_factory=db.provided.session)
    stack_repository = providers.Factory(StackRepository, session_factory=db.provided.session)
    
    advertiser_service = providers.Factory(AdvertiserService,  advertiser_repository=advertiser_repository)
    provider_service = providers.Factory(ProviderService,  provider_repository=provider_repository)
    job_service = providers.Factory(JobService,  job_repository=job_repository)
    stack_service = providers.Factory(StackService,  stack_repository=stack_repository)