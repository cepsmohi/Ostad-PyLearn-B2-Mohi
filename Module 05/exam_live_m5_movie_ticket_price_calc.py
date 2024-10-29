def calculate_ticket_price(age, showtime):
    if age <= 10:
        ticket_price = 300
    elif 11 <= age <= 25:
        ticket_price = 500
    elif 26 <= age <= 60:
        ticket_price = 800
    else:
        ticket_price = 400

    discount = 0

    if showtime < 1700:
        discount = 0.10 * ticket_price

    print(f"Ticket price: {ticket_price} BDT")
    print(f"Discount: {discount:.2f} BDT")
    print(f"Discounted Price: {ticket_price - discount:.2f} BDT")


age = int(input("Age: "))
showtime = int(input("Showtime (HHMM): "))
try:
    if age <= 0:
        raise ValueError("Age must be a positive integer.")

    hours = showtime // 100
    minutes = showtime % 100

    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError("Please provide the showtime in the correct format.")

    calculate_ticket_price(age, showtime)
except Exception as e:
    print(f"Invalid input: {e}")