import datetime

def calculate_due_amount():
    """Calculates the due amount, days overdue, and applies a late fee if necessary."""
    
    # 1. Get user inputs for dates and amount
    print("Enter dates in DD-MM-YYYY format.")
    try:
        today_str = input("Enter today's date (e.g., 01-01-2024): ")
        invoice_date_str = input("Enter the invoice date: ")
        due_date_str = input("Enter the payment due date: ")
        
        # Convert string inputs to datetime objects
        today = datetime.datetime.strptime(today_str, "%d-%m-%Y").date()
        invoice_date = datetime.datetime.strptime(invoice_date_str, "%d-%m-%Y").date()
        due_date = datetime.datetime.strptime(due_date_str, "%d-%m-%Y").date()
        
        total_amount = float(input("Enter the total invoice amount (e.g., 100.00): "))
    
    except ValueError as e:
        print(f"\nInvalid input: {e}. Please ensure dates are in DD-MM-YYYY format and amount is a number.")
        return

    # 2. Calculate days overdue
    if today > due_date:
        days_overdue = (today - due_date).days
        # Apply a 5% late fee
        late_fee = total_amount * 0.05
        new_total = total_amount + late_fee
        print(f"\n--- Invoice Details ---")
        print(f"Invoice Date: {invoice_date}")
        print(f"Original Due Date: {due_date}")
        print(f"Today's Date: {today}")
        print(f"Original Amount: ${total_amount:.2f}")
        print(f"Days Overdue: {days_overdue} days")
        print(f"Late Fee (5%): ${late_fee:.2f}")
        print(f"**Total Due Amount (including late fee): ${new_total:.2f}**")
    else:
        days_until_due = (due_date - today).days
        print(f"\n--- Invoice Details ---")
        print(f"Invoice Date: {invoice_date}")
        print(f"Due Date: {due_date}")
        print(f"Total Due Amount: ${total_amount:.2f}")
        if days_until_due >= 0:
             print(f"Days remaining until due: {days_until_due} days. No late fee applied.")
        else:
             print(f"Payment is due today. No late fee applied yet.")


# Run the function when the script is executed
if __name__ == "__main__":
    calculate_due_amount()