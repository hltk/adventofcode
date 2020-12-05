Input = open('10.in').readlines

points = Input.map { |l| l.scan(/-?\d+/).map(&:to_i) }

t = 0
loop do
  rx = points.map { |l| l[0] }.minmax
  ry = points.map { |l| l[1] }.minmax
  if [rx[1] - rx[0], ry[1] - ry[0]].max <= 100
    puts t
    grid = Array.new(ry[1] - ry[0] + 1) { Array.new(rx[1] - rx[0] + 1) { '.' } }
    points.each { |a, b, _, _| grid[b - ry[0]][a - rx[0]] = '#' }
    puts grid.map(&:join).join("\n")
  end
  t += 1
  points.map! { |a, b, c, d| [a + c, b + d, c, d] }
end
