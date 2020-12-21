Input = open('06.in').readlines.map { |l| l.split.map(&:to_i) }

MinX, MaxX = Input.map(&:first).minmax
MinY, MaxY = Input.map(&:last).minmax

def dist(a, b)
  (a[0] - b[0]).abs + (a[1] - b[1]).abs
end

def solve(b)
  area = [0] * Input.length
  ((MinX - b)..(MaxX + b)).each do |x|
    ((MinY - b)..(MaxY + b)).each do |y|
      c = [x, y]
      best = Input.min { |a, b| dist(a, c) <=> dist(b, c) }
      next if Input.count { |a| dist(a, c) == dist(best, c) } > 1
      area[Input.find_index(best)] += 1
    end
  end
  area
end

A = solve(200)
B = solve(201)

vals = A.zip(B).select { |a, b| a == b }

puts vals.max.first

def area(b)
  s = 0
  ((MinX - b)..(MaxX + b)).each do |x|
    ((MinY - b)..(MaxY + b)).each do |y|
      s += 1 if Input.map { |a| dist(a, [x, y]) }.sum < 10_000
    end
  end
  s
end

puts area(400)
