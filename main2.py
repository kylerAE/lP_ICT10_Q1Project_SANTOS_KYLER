from pyscript import document

def create_order(event):
    total = 0
    selected_items = []

    for i in range(1, 6):
        checkbox = document.getElementById(f"item{i}")
        if checkbox.checked:
            total += float(checkbox.value)
            selected_items.append(checkbox.nextSibling.textContent.strip())

    name = document.getElementById("customer_name").value
    email = document.getElementById("customer_email").value

    if not name or not email:
        document.getElementById("output").innerHTML = "<p style='color:red;'>Please fill out all fields.</p>"
        return

    summary = f"""
    <h3>Order Summary</h3>
    <p><b>Name:</b> {name}</p>
    <p><b>Email:</b> {email}</p>
    <p><b>Items:</b> {', '.join(selected_items)}</p>
    <p><b>Total:</b> ₱{total:.2f}</p>
    """

    document.getElementById("output").innerHTML = summary