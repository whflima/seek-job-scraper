from selenium import webdriver

from app.models.filters import Filters
from app.spiders.search_bar.fields.classification import Classification
from app.spiders.search_bar.fields.keywords import Keywords
from app.spiders.search_bar.fields.location import Location

class SearchBar:
    def __init__(self, driver: webdriver, keywords: str, classification: str, location: str):
        self.driver = driver
        self.keywords = Keywords(driver=driver, value=keywords) 
        self.classification = Classification(driver=driver, value=classification) 
        self.location = Location(driver=driver, value=location) 

    def get_keywords(self) -> str:
        return self.keywords.get_value()
    
    def get_classification(self) -> str:
        return self.classification.get_value()
    
    def get_location(self) -> str:
        return self.location.get_value()
    
    def get_values(self) -> Filters:
        return Filters(
            keywords = self.get_keywords(),
            classification = self.get_classification(),
            location = self.get_location()
        )
    
    def set_value(self, keywords: str, classification: str, location: str) -> None:
        self.keywords.set_value(keywords)
        self.classification.set_value(classification)
        self.location.set_value(location)
        
    def apply_filters(self) -> None:
        self.keywords.apply_filter()
        self.classification.apply_filter()
        self.location.apply_filter()
        self.search_results()
        
    def search_results(self) -> None:
        return None
