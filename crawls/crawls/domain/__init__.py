from symbol import import_from
import scrapy
from dataclasses import dataclass

@dataclass
class ChapterDTO:

    index: int = None
    name: str = None 
    url: str = None
    content: str = None