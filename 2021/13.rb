require './utils'

a, b = read(13, 2021).split "\n\n"
a, b = [a, b].map { |x| x.split "\n" }

points = a.map { |x|
  x, y = x.split(",").map &:to_i
  [y, x]
}

b.each do |l|
  fx,* = l.ints
  points = points.map { |y, x|
    /x=/ =~ l ? [y, x > fx ? fx - (x - fx) : x] : [y > fx ? fx - (y - fx) : y, x]
  }.uniq
end

my = points.map(&:first).max + 1
mx = points.map(&:last).max + 1

grid = Array.new(my, [])
grid.map! { |x| x = Array.new(mx, ".") }
points.each do |y, x|
  grid[y][x] = "#"
end

puts grid.map(&:join).join("\n")
