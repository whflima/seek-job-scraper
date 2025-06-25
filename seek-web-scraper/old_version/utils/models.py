from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Filters:
    keywords: str = ""
    location: str = ""
    time: str = ""
    classification: str = ""
    sort: str = ""

@dataclass
class Data:
    filters: Optional[Filters] = None
    additional_filters: Optional[list[str]] = None
    save_result: bool = False
    return_result: bool = False

@dataclass
class WebsiteProvider:
    name: str
    website_provider_id: Optional[int] = None

@dataclass 
class Advertiser:
    name: str
    advertiser_id: Optional[int] = None

@dataclass
class WebsiteProviderAdvertiser:
    website_provider_id: int
    advertiser_id: int

@dataclass
class Job:
    title: str
    job_id: Optional[int] = None
    advertiser_id: Optional[int] = None
    link: Optional[str] = None
    description: Optional[str] = field(default=None, repr=False)

@dataclass
class TechStack:
    category: str
    subcategory: str
    stack: str
    tech_stack_id: Optional[int] = None

@dataclass
class JobTechStack:
    job_id: int
    tech_stack_id: int

@dataclass
class JobCard:
    job: Job
    advertiser: Advertiser
    stacks: list[TechStack]