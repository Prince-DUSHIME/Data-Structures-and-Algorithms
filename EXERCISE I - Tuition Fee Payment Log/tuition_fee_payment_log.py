
# Integers: Tuition fee payments (in dollars)
tuition_payments = [1200, 1500, 1300, 1400, 1600]
total_payment = sum(tuition_payments)
average_payment = total_payment / len(tuition_payments)
min_payment = min(tuition_payments)
max_payment = max(tuition_payments)

# Strings: Formatted report
report = (
    f"Tuition Fee Payment Log Report\n"
    f"Total Payments: ${total_payment}\n"
    f"Average Payment: ${average_payment:.2f}\n"
    f"Minimum Payment: ${min_payment}\n"
    f"Maximum Payment: ${max_payment}\n"
)
print(report)

# Booleans: Threshold check
threshold = 1350
if average_payment > threshold and max_payment > 1500:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists: Maintain and modify records
students = ["Alice", "Bob", "Charlie", "David"]
print("Original list:", students)
students.append("Eve")
students = [s for s in students if s != "Bob"]  # Remove 'Bob'
students.sort()
print("Modified list:", students)

# Arrays: Store a subset and compare sums
payment_array = array.array('i', tuition_payments[:3])
array_sum = sum(payment_array)
print(f"Sum of array subset: {array_sum}")
print(f"Sum of list subset: {sum(tuition_payments[:3])}")

# Dictionaries: List of payment records
payment_records = [
    {'id': 1, 'name': 'Alice', 'value': 1200},
    {'id': 2, 'name': 'Bob', 'value': 1500},
    {'id': 3, 'name': 'Charlie', 'value': 1300}
]
# Update Charlie's payment
for record in payment_records:
    if record['name'] == 'Charlie':
        record['value'] = 1350
# Delete Bob's record
payment_records = [rec for rec in payment_records if rec['name'] != 'Bob']
# Compute total value
total_value = sum(rec['value'] for rec in payment_records)
print(f"Total value from records: ${total_value}")