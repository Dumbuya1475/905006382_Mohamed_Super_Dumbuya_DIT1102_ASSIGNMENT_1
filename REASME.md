# Citizen Complaint System (DPG Compliant)

**Course:** PROG211 - Object-Oriented Programming 1  
**Module Code:** PROG211  
**Institution:** Limkokwing University of Creative Technology, Sierra Leone  

---

## Overview
The **Citizen Complaint System** is a lightweight, open-source Python application built using Object-Oriented Programming (OOP) principles. It enables citizens to log public infrastructure and governance issues while remaining fully compliant with Digital Public Goods (DPG) standards.

---

## Digital Public Goods (DPG) Alignment

1. **Open-Source:** Source code is fully accessible and uploaded to GitHub under an open license.
2. **Privacy-Respecting:** The system adheres strictly to data minimization principles. No Personally Identifiable Information (PII) such as full names, phone numbers, or residential addresses are stored. All records utilize pseudonymous identifier tags (`citizen_id`).
3. **Modular and Reusable:** Built with object-oriented encapsulation, enabling smooth expansion across different municipal or national public service departments.

---

## System Architecture & OOP Concepts Applied

- **Classes Used:**
  - `Citizen`: Handles citizen identification attributes (anonymized) and location domain.
  - `Complaint`: Handles system issue reports, status transitions, and class-level accounting.
- **Methods Implemented:**
  - **Instance Methods:** `resolve_complaint()`, `display_info()`
  - **Class Method:** `get_total_complaints()` via `@classmethod`
- **Data Structure:** Python `dict` mapping unique `complaint_id` keys to object instances for $O(1)$ key lookup efficiency.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/Dumbuya1475/Citizen-Complaint-System.git](https://github.com/YOUR_GITHUB_USERNAME/Citizen-Complaint-System.git)