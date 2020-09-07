import copy


BITMAPS = {
    'crab': [
        "--o-----o--",
        "---o---o---",
        "--ooooooo--",
        "-oo-ooo-oo-",
        "ooooooooooo",
        "o-ooooooo-o",
        "o-o-----o-o",
        "---oo-oo---",
    ],
    'squid': [
        "---oo---",
        "--oooo--",
        "-oooooo-",
        "oo-oo-oo",
        "oooooooo",
        "--o--o--",
        "-o-oo-o-",
        "o-o--o-o",
    ],
}
MAX_SPRITE_WIDTH = len(BITMAPS['crab'][0])
MAX_SPRITE_LENGTH = len(BITMAPS['crab'])


class SpaceInvader:

    def __init__(self, bitmap):
        self.bitmap = copy.deepcopy(bitmap)
        # max_pixels = cols * rows
        self.max_pixels = len(self.bitmap) * len(self.bitmap[0])

    def match(self, other):
        matched_pixels = 0
        # lines
        for l1, l2 in zip(self.bitmap, other.bitmap):
            # individual pixels
            for p1, p2 in zip(l1, l2):
                matched_pixels += 1 if p1 == p2 else 0
        return matched_pixels / self.max_pixels


class Squid(SpaceInvader):

    def __init__(self):
        super().__init__(BITMAPS['squid'])


class Crab(SpaceInvader):

    def __init__(self):
        super().__init__(BITMAPS['crab'])


class InvaderFactory:

    def __init__(self, radar):
        self.radar = radar

    def __call__(self):
        return self._generate()

    def _generate(self):
        rows = []
        for i in range(self.radar.pos_y, self.radar.upper_y_limit):
            bit = self.radar.bitmap[i][self.radar.pos_x : self.radar.upper_x_limit]
            if bit:
                rows.append(bit)
        self.radar.next()
        # return None if the generator is exhausted
        return SpaceInvader(rows) if rows else None


CRAB = Crab()
SQUID = Squid()
