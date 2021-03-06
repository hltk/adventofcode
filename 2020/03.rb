require './utils.rb'
@grid = read(3).split

def calc(xs, ys)
  (0...@grid.length).step(ys).with_index.count do |y, x|
    @grid[y][(x * xs) % @grid[0].length] == '#'
  end
end

p calc(3, 1)
p [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]].map { |a, b| calc(a, b) }.inject :*
