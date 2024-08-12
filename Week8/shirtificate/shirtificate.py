from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()


        self.set_font("helvetica", "B", 50)
        self.cell(0, 75, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


        self.image("shirtificate.png", x=30  ,y=100 , w=150, h=150)


        self.set_font("helvetica", "B", size=23)
        self.set_text_color(255, 255, 255)
        self.cell(0, 150, border=0, align="C", text=f"{name} took CS50")

    def polygon(self, points, style=''):
        self._out(' '.join(f'{x} {self.h - y}' for x, y in points) + ' ' + style + ' re')





def main():
    name = input("What is your name? ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
