require './utils'

class String
  def ints
    self.scan(/\d+/).map &:to_i
  end
end


def points(x1, y1, x2, y2)
  return ([y1, y2].min..[y1, y2].max).map { |y|
    [x1, y]
  } if x1 == x2
  x1, y1, x2, y2 = [x2, y2, x1, y1] if x1 > x2
  return (x1..x2).map { |x|
    [x, y1 + (x - x1) * (y2 - y1).clamp(-1, 1)]
  }
end

d = read(5, 2021).split "\n"
d = d.map &:ints
d = d.flat_map { |x| points(*x) }
p d.tally.count { _2 > 1 }
