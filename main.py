from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
import random

class mainScreen(MDFloatLayout):
    result = [0,0,0,0,0,0,0,0,0]


    btn0 = ObjectProperty()
    btn1 = ObjectProperty()
    btn2 = ObjectProperty()
    btn3 = ObjectProperty()
    btn4 = ObjectProperty()
    btn5 = ObjectProperty()
    btn6 = ObjectProperty()
    btn7 = ObjectProperty()
    btn8 = ObjectProperty()

    label = ObjectProperty()
    sorte = random.randrange(2)

    turns = 0
    endGame = True

    def ai(self):
        self.turns += 1

        while True and self.endGame:
            n = random.randrange(9)
            print(n)
            if n == 0 and self.result[n] == 0:
                self.btn0.text = "O"
                self.btn0.disabled = True
                self.result[n] =6
                break

            if n == 1 and self.result[n] == 0:
                self.btn1.text = "O"
                self.btn1.disabled = True
                self.result[n] =6
                break

            if n == 2 and self.result[n] == 0:
                self.btn2.text = "O"
                self.btn2.disabled = True
                self.result[n] =6
                break

            if n == 3 and self.result[n] == 0:
                self.btn3.text = "O"
                self.btn3.disabled = True
                self.result[n] =6
                break

            if n == 4 and self.result[n] == 0:
                self.btn4.text = "O"
                self.btn4.disabled = True
                self.result[n] =6
                break

            if n == 5 and self.result[n] == 0:
                self.btn5.text = "O"
                self.btn5.disabled = True
                self.result[n] =6
                break

            if n == 6 and self.result[n] == 0:
                self.btn6.text = "O"
                self.btn6.disabled = True
                self.result[n] =6
                break

            if n == 7 and self.result[n] == 0:
                self.btn7.text = "O"
                self.btn7.disabled = True
                self.result[n] =6

                break
            if n == 8 and self.result[n] == 0:
                self.btn8.text = "O"
                self.btn8.disabled = True
                self.result[n] =6
                break

        if self.turns == 9:
            self.tie()


    def btnPressed(self, btn):
        self.turns += 1
        btn.text = "X"

        btn.md_bg_color = 1, 1, 1
        btn.disabled = True
        self.result[ btn.position ] = 1

        if self.turns == 9:
            self.tie()

    def checkResult(self):
        print(self.result)
        finalCheck = self.result[0] + self.result[4] + self.result[8]

        if finalCheck == 3:
            self.win()

        elif finalCheck == 18:
            self.lost()


        finalCheck =  self.result[2] +  self.result[4] +  self.result[6]

        if finalCheck == 3:
            self.win()

        elif finalCheck == 18:
            self.lost()

#   Check the rows
        for i in range(0,9,3):
            finalCheck =  0
            for j in range(3):
                finalCheck = finalCheck + self.result[j+i]

            if finalCheck == 3:
                self.win()

            elif finalCheck == 18:
                self.lost()


#   Check the columns
        for i in range(3):
            finalCheck = 0

            for j in range(0,9,3):
                finalCheck = finalCheck + self.result[j+i]

            if finalCheck == 3:
                self.win()

            elif finalCheck == 18:
                self.lost()


    def win(self):
        self.label.text = "win"
        self.disableAllBtns()
        self.endGame = False

    def lost(self):
        self.label.text = "lost"
        self.disableAllBtns()
        self.endGame = False

    def disableAllBtns(self):
        self.btn0.disabled = True
        self.btn1.disabled = True
        self.btn2.disabled = True
        self.btn3.disabled = True
        self.btn4.disabled = True
        self.btn5.disabled = True
        self.btn6.disabled = True
        self.btn7.disabled = True
        self.btn8.disabled = True


    def tie(self):
        self.label.text ="tie"
        self.disableAllBtns()
        self.endGame = False

    def restart(self):
        self.endGame = True
        self.result=[0,0,0,0,0,0,0,0,0]
        self.turns = 0
        self.btn0.disabled = False
        self.btn1.disabled = False
        self.btn2.disabled = False
        self.btn3.disabled = False
        self.btn4.disabled = False
        self.btn5.disabled = False
        self.btn6.disabled = False
        self.btn7.disabled = False
        self.btn8.disabled = False

        self.btn0.text = ""
        self.btn1.text = ""
        self.btn2.text = ""
        self.btn3.text = ""
        self.btn4.text = ""
        self.btn5.text = ""
        self.btn6.text = ""
        self.btn7.text = ""
        self.btn8.text = ""
        self.label.text = ""

        self.btn0.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0] #       self.btn1.md_bg_color= app.theme_cls.primary_color
        self.btn1.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0] #       self.btn1.md_bg_color= app.theme_cls.primary_color
        self.btn2.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0]
        self.btn3.md_bg_color=[0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0]
        self.btn4.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0]
        self.btn5.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0]
        self.btn6.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0] #       self.btn7.md_bg_color=[0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0]
        self.btn7.md_bg_color= [0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0] #       self.btn1.md_bg_color= app.theme_cls.primary_color
        self.btn8.md_bg_color=[0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0]
    #if sorte:
    #    print(f"sorte {sorte}")
    #    self.ai()

class app(MDApp):
#    print(f"essa e a cor { app.theme_cls.primary_colo}")
    ...
app().run()
