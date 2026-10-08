"""
PROG211: Object-Oriented Programming 1
Assignment: Citizen Complaint System (Digital Public Goods Standard)

Domain: Government (Citizen Complaint System)
DPG Compliance:
- Open-Source & Modular Architecture
- Privacy-Respecting: Uses anonymized Citizen IDs instead of personal details
"""


class Citizen:
    """Represents a citizen issuing a complaint using anonymized identifiers."""

    def __init__(self, citizen_id: str, district: str):
        self.citizen_id = citizen_id  # Anonymized ID to respect privacy
        self.district = district

    def display_info(self) -> None:
        """Instance method to display anonymized citizen details."""
        print(f"Citizen ID: {self.citizen_id} | District: {self.district}")


class Complaint:
    """Represents a public service complaint filed by a citizen."""

    total_complaints = 0  # Class attribute for tracking count

    def __init__(self, complaint_id: str, citizen: Citizen, category: str, description: str):
        self.complaint_id = complaint_id
        self.citizen = citizen  # Object interaction / association
        self.category = category
        self.description = description
        self.status = "Pending"
        
        Complaint.total_complaints += 1

    def resolve_complaint(self) -> None:
        """Instance method to update complaint status."""
        self.status = "Resolved"
        print(f"Complaint {self.complaint_id} has been marked as Resolved.")

    def display_info(self) -> None:
        """Instance method to display full complaint details."""
        print(f"[Complaint ID: {self.complaint_id}]")
        print(f"  Category: {self.category}")
        print(f"  Description: {self.description}")
        print(f"  Status: {self.status}")
        self.citizen.display_info()

    @classmethod
    def get_total_complaints(cls) -> int:
        """Class method returning total complaints created."""
        return cls.total_complaints


# --- Data Structure Integration (Task 2: Dictionary implementation) ---
# Dictionary to store complaints using unique complaint_id as the key
complaint_registry: dict[str, Complaint] = {}


def add_complaint(complaint: Complaint) -> None:
    """Adds a complaint object to the central registry dictionary."""
    complaint_registry[complaint.complaint_id] = complaint
    print(f"Successfully registered Complaint ID: {complaint.complaint_id}")


def display_all_complaints() -> None:
    """Iterates through and displays all registered complaints."""
    print("\n" + "=" * 40)
    print("      PUBLIC COMPLAINT REGISTRY LOG      ")
    print("=" * 40)
    if not complaint_registry:
        print("No complaints recorded.")
        return

    for complaint_id, complaint_obj in complaint_registry.items():
        complaint_obj.display_info()
        print("-" * 40)


# --- Demonstration of Program Execution ---
if __name__ == "__main__":
    # 1. Object Creation & Interaction
    citizen_1 = Citizen(citizen_id="CIT-1042", district="Western Area Urban")
    citizen_2 = Citizen(citizen_id="CIT-8821", district="Bo District")

    complaint_1 = Complaint(
        complaint_id="CMP-001",
        citizen=citizen_1,
        category="Sanitation",
        description="Waste management overflow at local market."
    )

    complaint_2 = Complaint(
        complaint_id="CMP-002",
        citizen=citizen_2,
        category="Road Infrastructure",
        description="Pothole obstruction on main arterial street."
    )

    # 2. Add Records to Dictionary Data Structure
    print("\n--- Registering Complaints ---")
    add_complaint(complaint_1)
    add_complaint(complaint_2)

    # 3. Display Records from Data Structure
    display_all_complaints()

    # 4. Demonstrate Method Execution
    print("\n--- Updating Status ---")
    complaint_1.resolve_complaint()

    # 5. Class Method Execution
    print(f"\nTotal Complaints Logged across System: {Complaint.get_total_complaints()}")