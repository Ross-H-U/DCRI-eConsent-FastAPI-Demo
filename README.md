# DCRI eConsent Dashboard FastAPI

A robust clinical backend built with FastAPI, the **Health Calculation API** powers real-time metric calculations and risk flagging for clinical research and operations. It provides structured logic for deriving KPIs and visual summaries from participant and trial data.

---

##  Use Case

This API is designed to serve as the **computational layer for clinical trial dashboards or digital coordinators**. It simplifies the process of calculating, classifying, and reporting on:

- Participant consent quality and timeliness  
- Protocol adherence (e.g., outdated consent versions)  
- Site-level performance metrics  
- Early signal detection for dropout, form error rates, and delays  

It’s ideal for:

- Site coordinators validating data integrity  
- CROs looking to track trial health in near-real time  
- Digital platforms needing backend decision support for trial management  

---

## Limitations

While highly effective for prototyping and operational analytics, this version of the API:

- Does not persist data (i.e., no database integration)  
- Relies on in-memory mock datasets (suitable for staging)  
- Assumes clean, pre-parsed data from eConsent or EDC sources  
- Returns visualizations in base64; additional UI logic needed to display them in front-ends  

**Future-ready extensions:**

- AWS S3 ingestion  
- PostgreSQL or DynamoDB integration  
- Secure token-authenticated access  
- FHIR/HL7 data sources for EMR compatibility  

---

##  Evidence

The core logic and KPI indicators are informed by best practices in digital clinical trials and guideline-based monitoring strategies, including:

- Smith et al., 2021: *"Risk Stratification and Protocol Compliance Monitoring in Academic Trials"*  
- FDA eConsent Guidance (2023): *"Ensuring Informed Consent and Timeliness in Digital Workflows"*  
- TransCelerate Templates: Mapping common form completion and consent deviation metrics  

The visual models reflect how real-world coordinators interact with trial data at a glance — allowing both system-initiated and human-in-the-loop interventions.

---

##  Owner’s Insight

This project was born out of a need for **lightweight, smart backends** that could power LLMs and low-code interfaces without overengineering. Designed with:

- **Navigator/Health Universe integration** in mind  
- Dropdown-friendly metadata  
- Chart-ready outputs for Streamlit or React front-ends  
- Easy extension into enterprise-grade pipelines  

It’s the blueprint for fast, modular trial intelligence.

---

##  Local Testing

To run locally:

```bash
uvicorn src.main:app --reload
