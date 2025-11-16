import turtle
from me_f9rmoi import ME_var, ME_ido


class MEjatek:

    def __init__(self, ablak):
        self.eredmenyek = []
        self.probaszam = 0
        self.max_proba = 3

        self.ablak = ablak
        self.ablak.bgcolor("maroon")
        self.ablak.title("Reakcióidő játék")

        self.felirat = turtle.Turtle()
        self.felirat.hideturtle()
        self.felirat.color("black")
        self.felirat.penup()
        self.felirat.goto(0, 0)

        self.var_ido = 0
        self.start_ido = 0
        self.aktiv = False

        self.kezdokep()

    def kezdokep(self, x=None, y=None):
        self.eredmenyek = []
        self.probaszam = 0
        self.max_proba = 3

        self.felirat.clear()
        self.felirat.color("black")
        self.ablak.bgcolor("maroon")
        self.ablak.title("ME Reakcióidő játék F9RMOI")

        self.felirat.goto(0, 60)
        self.felirat.write("Reakció teszt!\n", align="center", font=("Arial", 20, "bold"))

        self.felirat.goto(0, 20)
        self.felirat.write("Nyomd meg az I billentyűt a játék indításához!\n", align="center",
                           font=("Arial", 15, "normal"))

        self.felirat.goto(0, -20)
        self.felirat.write("Játék elkezdése után várnod kell hogy zöld legyen a képernyő és kattinthas!",
                           align="center", font=("Arial", 12, "italic"))

        self.felirat.goto(0, -100)
        self.felirat.write("Kilépéshez nyomd meg: Escape\n", align="center", font=("Arial", 10, "italic"))

        self.ablak.onkey(self.inditas, "i")
        self.ablak.onkey(self.ablak.bye, "Escape")
        self.ablak.listen()

    def inditas(self):
        self.ablak.bgcolor("black")
        self.felirat.color("white")
        self.felirat.clear()

        self.var_ido = ME_var(2, 5)
        self.ablak.ontimer(self.inditas_2, self.var_ido * 1000)

    def inditas_2(self):
        self.ablak.bgcolor("green")
        self.felirat.write("KATTINTS MOST!", align="center", font=("Arial", 20, "normal"))
        self.start_ido = ME_ido()
        self.aktiv = True
        self.ablak.onscreenclick(self.meres)

    def mentes(self, szoveg):
        from me_f9rmoi import ME_mentes
        siker = ME_mentes(szoveg)


    def meres(self, x, y):
        if not self.aktiv:
            return

        vege = ME_ido()
        reakcio = vege - self.start_ido

        self.eredmenyek.append(reakcio)
        self.probaszam += 1

        if self.probaszam == self.max_proba:
            atlag = sum(self.eredmenyek) / self.max_proba

            szoveg = f"Utolsó: {reakcio:.3f} mp | Átlag: {atlag:.3f} mp"
            self.mentes(szoveg)

            self.felirat.clear()
            self.ablak.bgcolor("black")

            self.felirat.goto(0, 40)
            self.felirat.write(f"Utolsó reakcióidőd: {reakcio:.3f} mp", align="center", font=("Arial", 15, "normal"))

            self.felirat.goto(0, 0)
            self.felirat.write(f"Átlag reakcióidőd: {atlag:.3f} mp", align="center", font=("Arial", 20, "normal"))

            self.felirat.goto(0, -40)
            self.felirat.write("Vége a játéknak.\nNyomd meg az I billentyűt az új játékhoz.", align="center",
                               font=("Arial", 12, "normal"))

            self.aktiv = False
            self.ablak.onkey(self.kezdokep, "i")
            return



        self.felirat.clear()
        self.ablak.bgcolor("black")
        self.felirat.goto(0, 0)
        self.felirat.write(
            f"Reakcióidő: {reakcio:.3f} mp\nNyomd meg az I-t az újabb próbához!\n({self.probaszam}/{self.max_proba} próbálkozás)",
            align="center", font=("Arial", 16, "normal")
        )

        self.aktiv = False
        self.ablak.onkey(self.inditas, "i")





