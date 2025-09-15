from js import document 

def calculate_area(event=None):
    try:
        base1 = float(Element("base1").element.value)
        base2 = float(Element("base2").element.value)
        height = float(Element("height").element.value)

        area = (base1 + base2) / 2 * height
        Element("trapezoid-area").element.innerText = f"{area:.2f}"
    except:
        Element("trapezoid-area").element.innerText = "Invalid input"

# Attach button click event
Element("calcBtn").element.onclick = calculate_area

