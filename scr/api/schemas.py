from pydantic import BaseModel, Field
from typing import Optional, Literal, List, Dict

class ReportInput(BaseModel):
    trial: Literal["T001"] = Field(..., description="Trial ID")
    site: Optional[Literal["All", "Seattle", "Chicago"]] = "All"
    coordinator: Optional[Literal["All", "NP Lee", "Dr Smith"]] = "All"
    method: Optional[Literal["All", "Remote", "In-Person"]] = "All"
    show_flags_only: Optional[bool] = Field(False, description="Show only flagged records")

class KPIResult(BaseModel):
    average_consent_time: str = Field(..., description="Average time from consent to enrollment")
    late_consents: int = Field(..., description="Number of participants with late consent")
    form_error_rate: str = Field(..., description="Percentage of form errors")
    withdrawn: int = Field(..., description="Number of participants who withdrew")

class ParticipantRecord(BaseModel):
    TrialID: str
    Site: str
    Coordinator: str
    ParticipantID: str
    ConsentStatus: str
    ConsentDate: str
    EnrollmentDate: str
    ConsentMethod: str
    ConsentVersion: str
    ProtocolVersionAtConsent: str
    FormsComplete: bool
    Withdrawn: bool
    MissingConsent: bool
    LateConsent: bool
    OutdatedProtocol: bool
    Flagged: bool

class ReportResponse(BaseModel):
    kpis: KPIResult
    records: List[ParticipantRecord]
    charts_base64: Dict[str, str]

    class Config:
        schema_extra = {
            "format": "display"
        }
