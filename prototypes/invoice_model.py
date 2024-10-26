from dataclasses import dataclass, field
from typing import List

@dataclass
class Part:
    name: str
    unit_price: float
    quantity: int
    core_charge: float = 0.0  # Core charge for specific parts (e.g., batteries, alternators)

    @property
    def total_price(self) -> float:
        return (self.unit_price * self.quantity) + self.core_charge

@dataclass
class Labor:
    description: str
    hours: float
    hourly_rate: float

    @property
    def total_price(self) -> float:
        return self.hours * self.hourly_rate

@dataclass
class Fee:
    description: str
    amount: float

@dataclass
class Invoice:
    parts: List[Part] = field(default_factory=list)
    labor: List[Labor] = field(default_factory=list)
    fees: List[Fee] = field(default_factory=list)
    
    @property
    def parts_subtotal(self) -> float:
        return sum(part.total_price for part in self.parts)

    @property
    def labor_subtotal(self) -> float:
        return sum(labor.total_price for labor in self.labor)

    @property
    def fees_total(self) -> float:
        return sum(fee.amount for fee in self.fees)

    @property
    def grand_total(self) -> float:
        return self.parts_subtotal + self.labor_subtotal + self.fees_total

    def parts_to_array(self) -> List[List]:
        return [
            [part.name, part.unit_price, part.quantity, part.core_charge, part.total_price]
            for part in self.parts
        ]
    
    def labor_to_array(self) -> List[List]:
        return [
            [l.description, l.hours, l.hourly_rate]
            for l in self.labor
        ]
    


    def summary(self) -> dict:
        # Generate a summary for easy review of each section
        return {
            "Parts Subtotal": self.parts_subtotal,
            "Labor Subtotal": self.labor_subtotal,
            "Fees Total": self.fees_total,
            "Grand Total": self.grand_total
        }
