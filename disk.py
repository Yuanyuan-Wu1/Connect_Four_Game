import time


class Disk:

    def __init__(self, x, y, color, radius):
        """inition the disk"""
        self.x = x
        self.y = y
        self.y_vel = 0.1
        self.radius = radius   # cell.size /2
        self.is_dropping = False  # true --> dropping
        self.dropped = False     # true ---> constantly display is fixed position
        self.color = color
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        if color == "RED":
            self.color = self.RED
        else:
            self.color = self.YELLOW

    def draw_disk(self):
        """draw the disk"""
        noStroke()
        # strokeWeight(0)
        fill(*self.color)
        ellipse(self.x * self.radius * 2 + self.radius,
                self.y * self.radius * 2 + self.radius,
                self.radius*1.5, self.radius*1.5)

    # if mouse released, disk. is_dropping = True --->disk.draw_drop_disk
    def drop_disk(self, target_y):
        # print("drop_disk")
        if not self.is_dropping:
            self.y = target_y+1
            self.draw_disk()
            self.is_dropping = True
            self.dropped = True
