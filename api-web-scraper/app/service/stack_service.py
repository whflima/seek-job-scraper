from app.repository.stack_repository import StackRepository
from app.dependencies.stack_filters import StackFilters
from app.dependencies.pagination_params import PaginationParams

class StackService():
    def __init__(self, stack_repository: StackRepository):
        self.stack_repository = stack_repository
    
    def get_all(self):
        return self.stack_repository.get_all()
    
    def get_stack(self, filters: StackFilters, pagination: PaginationParams):
        return self.stack_repository.get_stack(filters, pagination)