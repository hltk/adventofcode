# Part 1

Input = open('11.in').read.to_i

def p(x, y)
  ((x + 10) * y + Input) * (x + 10) / 100 % 10 - 5
end

R = (1..300).to_a
C = R.product(R)

G = Array.new(301) { Array.new(301) { 0 } }

C.each do |x, y|
  G[x][y] = G[x - 1][y] + G[x][y - 1] - G[x - 1][y - 1] + p(x, y)
end

def r(x, y, s)
  return -Float::INFINITY if [x, y].max + s - 1 > 300

  G[x + s - 1][y + s - 1] + G[x - 1][y - 1] - G[x + s - 1][y - 1] - G[x - 1][y + s - 1]
end

ans = C.max { |a, b| r(*a, 3) <=> r(*b, 3) }

puts ans.join(',')

# Part 2

ans = C.map do |x, y|
  [x, y, R.max { |a, b| r(x, y, a) <=> r(x, y, b) }]
end.max { |a, b| r(*a) <=> r(*b) }

puts ans.join(',')
