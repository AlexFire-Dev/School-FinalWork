class Button:

    def __init__(self, canvas, pos_x, pos_y, width, height, function=None, text=None, font=None, anchor='c'):

        if anchor == 'w':
            self.x = pos_x + width / 2
            self.y = pos_y
        elif anchor == 'e':
            self.x = pos_x - width / 2
            self.y = pos_y
        elif anchor == 'n':
            self.x = pos_x
            self.y = pos_y + height / 2
        elif anchor == 's':
            self.x = pos_x
            self.y = pos_y - height / 2
        elif anchor == 'nw':
            self.x = pos_x + width / 2
            self.y = pos_y + height / 2
        elif anchor == 'se':
            self.x = pos_x - width / 2
            self.y = pos_y - height / 2
        elif anchor == 'sw':
            self.x = pos_x + width / 2
            self.y = pos_y - height / 2
        elif anchor == 'ne':
            self.x = pos_x - width / 2
            self.y = pos_y + height / 2
        else:
            self.x = pos_x
            self.y = pos_y

        if function:
            function(canvas)

        self.text = text
        self.font = font

        canvas.create_rectangle(self.x-width/2, self.y-height/2, self.x+width/2, self.y+height/2)
        canvas.create_text(self.x, self.y, text=self.text, font=self.font)
