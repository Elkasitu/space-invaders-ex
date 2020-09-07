import invaders


class Radar:

    def __init__(self, bitmap):
        self.bitmap = bitmap
        self.pos_x = 0
        self.pos_y = 0
        self.max_x = len(self.bitmap[0])
        self.max_y = len(self.bitmap)

    def next(self):
        self.pos_x += 1
        if self.pos_x == self.max_x:
            self.pos_x = 0
            self.pos_y += 1

    @property
    def upper_y_limit(self):
        if self.pos_y + invaders.MAX_SPRITE_LENGTH > self.max_y:
            return self.max_y
        return self.pos_y + invaders.MAX_SPRITE_LENGTH

    @property
    def upper_x_limit(self):
        if self.pos_x + invaders.MAX_SPRITE_WIDTH > self.max_x:
            return self.max_x
        return self.pos_x + invaders.MAX_SPRITE_WIDTH
