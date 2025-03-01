from firecrawl import Firecrawl
from pydantic import BaseModel
from typing import List, Optional

class JobDescription(BaseModel):
    title: str
    company: str
    description: str
    responsibilities: List[str]
    skills_required: List[str]
    qualifications: List[str]

def scrape_job_description(url: str) -> Optional[JobDescription]:
    try:
        fc=Firecrawl()
        job_description=fc.scrape(url)
        return JobDescription(**job_description)
    except Exception as e:
        print(f"Error scraping job description: {e}")
        return None
    


    
        
        


