import Image, ImageDraw, ImageFont

class Drawer:


  def __init__(self, coords):
    # self.coords = wkt
    self.image = Image.new("RGBA", (800, 600))
    self.draw = ImageDraw.Draw(self.image)
    self.minx, self.miny, self.maxx, self.maxy = self.analyze_coords(coords)
    self.draw.polygon(self.coord_mapper(coords), outline='black', fill='white')


  def draw_poly(self, coords, out, fil):
    self.draw.polygon(self.coord_mapper(coords), outline=out, fill=fil)

  def draw_legend(self, number, temperature, fil):
    self.draw.rectangle((50, 400+number*15)+(60, 410+number*15), fill=fil)
    self.draw.text((70, 400+number*15), "temp less than %.02f deg. C" % temperature, font=ImageFont.load_default(), fill='black')


  def draw_points(self, coords, radius, fill='orange'):
    for coord in self.coord_mapper(coords):
      box = (coord[0] - radius, coord[1] - radius, coord[0] + radius, coord[1] + radius)
      self.draw.ellipse(box, fill=fill)


  def draw_line(self, coords, width, fill='red'):
    self.draw.line(self.coord_mapper(coords), width=width, fill=fill)


  def analyze_coords(self, coords):
    xs, ys = zip(*coords)
    minx = min(xs)
    miny = min(ys)
    return (minx, miny, max(xs) - minx, max(ys) - miny)


  def coord_mapper(self, coords):
    xs, ys = zip(*coords)
    xs = [x - self.minx for x in xs]
    ys = [y - self.miny for y in ys]
    xs = [x / self.maxx * 800 for x in xs]
    ys = [y / self.maxy * 600 for y in ys]
    return zip(xs, ys)


  def save(self, filename):
    return self.image.save(filename, "PNG")
