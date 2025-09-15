from js import document

def calculate_area(event=None):
    try:
        base1 = float(document.getElementById("base1").value)
        base2 = float(document.getElementById("base2").value)
        height = float(document.getElementById("height").value)

        area = (base1 + base2) / 2 * height
        document.getElementById("trapezoid-area").innerText = f"{area:.2f}"
    except:
        document.getElementById("trapezoid-area").innerText = "Invalid input"

# Attach button click event
document.getElementById("calcBtn").onclick = calculate_area
