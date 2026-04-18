from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ContactInfo(BaseModel):
    emails: List[str] = []
    phones: List[str] = []
    linkedin: List[str] = []
    github: List[str] = []

class CandidateAnalysis(BaseModel):
    Aday: str
    Skor: float
    Semantik_Skor: float
    Anahtar_Kelime_Skor: float
    Eşleşen_Yetkinlikler: List[str]
    Eksik_Yetkinlikler: Optional[List[str]] = None
    Bolum_Skorlari: Dict[str, float]
    Bolum_Detaylari: Dict[str, str]
    Kanitlar: List[str]
    Iletisim: ContactInfo
    Etiket: str
    Ozet: str
    Mülakat_Soruları: List[str] = []

class ChatRequest(BaseModel):
    message: str
    results: List[CandidateAnalysis]
    job_description: str

class ChatResponse(BaseModel):
    reply: str
    filtered_candidates: Optional[List[str]] = None # Aday isimleri listesi

class AnalysisResponse(BaseModel):
    results: List[CandidateAnalysis]
    job_description: str

class EmailRequest(BaseModel):
    candidate: CandidateAnalysis
    company_name: str
    position_name: str
    interview_date: str

class EmailResponse(BaseModel):
    subject: str
    body: str
    mailto_link: str
