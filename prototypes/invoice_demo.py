from invoice_model import *

# Define parts
engine_part = Part(name="Engine Mount", unit_price=120.50, quantity=1, core_charge=20.00)
oil_filter = Part(name="Oil Filter", unit_price=15.00, quantity=2)

# Define labor
labor_replace_mount = Labor(description="Replace Engine Mount", hours=2.5, hourly_rate=85.00)
labor_oil_change = Labor(description="Oil Change", hours=0.5, hourly_rate=85.00)

# Define fees
disposal_fee = Fee(description="Oil Disposal Fee", amount=10.00)

# Create an invoice and add items
invoice = Invoice(
    parts=[engine_part, oil_filter],
    labor=[labor_replace_mount, labor_oil_change],
    fees=[disposal_fee]
)


print("Invoice Summary")
print("Parts Subtotal:", invoice.parts_subtotal)
print("Labor Subtotal:", invoice.labor_subtotal)
print("Fees Total:", invoice.fees_total)
print("Grand Total:", invoice.grand_total)


print("Detailed Invoice Summary:")
print(invoice.summary())
