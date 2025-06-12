from dataclasses import dataclass


@dataclass
class Filters:
    keywords: str
    classification: str
    location: str