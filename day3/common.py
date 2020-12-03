class Map:
    def __init__(self, filepath):
        #first index will be y, second is x
        self.data = list()
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                self.data.append(line)

        self.width = len(self.data[0])
        self.height = len(self.data)

        #Check that we loaded the map with the same width everywhere
        assert all([self.width == len(i) for i in self.data])

    def check(self, x, y):
        if y >= self.height:
            return None
        return self.data[y][x%self.width] == "#"

    def print(self):
        for line in self.data:
            print("".join(line))

class Sled:
    def __init__(self, map_):
        self.map = map_

    def go(self, xpos, ypos, step_x, step_y):
        count = 0
        status = self.map.check(xpos,ypos)
        while status is not None:
            xpos += step_x
            ypos += step_y
            status = self.map.check(xpos,ypos)
            if status:
                count += 1

        return count

