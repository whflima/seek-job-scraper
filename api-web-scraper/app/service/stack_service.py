from app.repository.stack_repository import StackRepository

class StackService():
    def __init__(self, stack_repository: StackRepository):
        self.stack_repository = stack_repository
    
    def get_all(self):
        return self.stack_repository.get_all()