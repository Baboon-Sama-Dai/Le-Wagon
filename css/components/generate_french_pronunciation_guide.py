from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Create a new PDF using reportlab which supports Unicode by default
pdf_path = "/mnt/data/French_Pronunciation_Guide.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# Helper function to write wrapped text
def draw_wrapped_text(text, x, y, max_width, line_height):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    lines = []
    current_line = ''
    for word in text.split():
        if stringWidth(current_line + ' ' + word, "Helvetica", 10) < max_width:
            current_line += ' ' + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    for line in lines:
        c.drawString(x, y, line)
        y -= line_height
    return y

# Title
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(width / 2, height - 50, "French Pronunciation Guide")

y = height - 80
c.setFont("Helvetica-Bold", 12)
c.drawString(40, y, "1. French Alphabet")
c.setFont("Helvetica", 10)
y -= 20
alphabet_data = """A - like "ah"
B - like "bay"
C - like "say"
D - like "day"
E - like "uh"
F - like "ef"
G - like "jay"
H - like "ash"
I - like "ee"
J - like "jay"
K - like "kah"
L - like "el"
M - like "em"
N - like "en"
O - like "oh"
P - like "pay"
Q - like "koo"
R - like "air"
S - like "ess"
T - like "tay"
U - like "oo"
V - like "vay"
W - like "doo-bluh-vay"
X - like "eeks"
Y - like "ee-grek"
Z - like "zed" """
y = draw_wrapped_text(alphabet_data.strip(), 40, y, width - 80, 14)

c.setFont("Helvetica-Bold", 12)
y -= 20
c.drawString(40, y, "2. Nasal Vowel Combinations")
c.setFont("Helvetica", 10)
y -= 20
nasal_data = """An, en - like "ah" (nasal)
On, om - like "awn" (nasal)
In, un - like "ang" (nasal) """
y = draw_wrapped_text(nasal_data.strip(), 40, y, width - 80, 14)

c.setFont("Helvetica-Bold", 12)
y -= 20
c.drawString(40, y, "3. Vowel Combinations")
c.setFont("Helvetica", 10)
y -= 20
vowel_data = """Ai - like "ay"
Au - like "oh"
Ei - like "ay"
Eu - like "uh"
Oe - like "uh" """
y = draw_wrapped_text(vowel_data.strip(), 40, y, width - 80, 14)

c.setFont("Helvetica-Bold", 12)
y -= 20
c.drawString(40, y, "4. Consonant Combinations")
c.setFont("Helvetica", 10)
y -= 20
consonant_data = """Ch - like "sh"
Gn - like "ny" (as in "canyon")
Ph - like "f"
Qu - like "kw" """
y = draw_wrapped_text(consonant_data.strip(), 40, y, width - 80, 14)

# Save PDF
c.save()

pdf_path
