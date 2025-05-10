from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.advertiser import Advertiser

class AdvertiserRepository():
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self._session_factory = session_factory
        self.model = Advertiser
    
    def get_all(self):
        with self._session_factory() as session:
            return session.query(self.model).all()