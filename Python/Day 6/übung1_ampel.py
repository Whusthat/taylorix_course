class Ampel():
    # a default 'Ampel' is red
    def __init__(self, red=True, yellow=False, green=False):
        self.red = red
        self.yellow = yellow
        self.green = green

    def show_current_color(self):
        if self.red:
            print('red')
        if self.yellow:
            print('yellow')
        if self.green:
            print('green')

    def set_red(self):
        self.red = True
        self.yellow = False
        self.green = False

    def set_green(self):
        self.red = False
        self.yellow = False
        self.green = True

    def set_yellow(self):
        self.red = False
        self.yellow = True
        self.green = False

    def set_yellow_red(self):
        self.red = True
        self.yellow = True
        self.green = False

    def switch(self):
        if self.green:
            self.set_yellow()
        elif self.yellow and self.red:
            self.set_green()
        elif self.yellow and not self.red:
            self.set_red()
        elif self.red and not self.yellow:
            self.set_yellow_red()
        self.show_current_color()


# create an 'Ampel'
ampel1 = Ampel()

# show current status = red
ampel1.show_current_color()
# switch to red-yellow
ampel1.switch()
# switch to green
ampel1.switch()
# switch to yellow
ampel1.switch()
# switch to red
ampel1.switch()