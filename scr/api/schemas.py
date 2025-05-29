from pydantic import BaseModel, Field

class KPIResult(BaseModel):
    average_consent_time: str = Field(..., description="Average time from consent to enrollment")
    late_consents: int = Field(..., description="Number of participants with late consent")
    form_error_rate: str = Field(..., description="Percentage of form errors")
    withdrawn: int = Field(..., description="Number of participants who withdrew")

class ReportResponse(BaseModel):
    kpis: KPIResult
    records: list
    charts_base64: dict

    class Config:
        schema_extra = {
            "format": "display"
        }
