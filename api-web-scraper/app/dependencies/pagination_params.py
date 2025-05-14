from fastapi import Query


class PaginationParams:
    def __init__(
        self,
        page: int = Query(1, ge=1, description="Page number"),
        limit: int = Query(10, ge=1, le=100, description="Max number of items to return")
    ):
        self.page = page
        self.limit = limit
        self.skip = (page - 1) * limit