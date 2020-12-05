# inspired by https://github.com/gjanee/advent-of-code-2018/blob/master/03.rb

class Claim
  attr_reader :id, :left, :top
  attr_accessor :overlaps
  def initialize(line)
    @id, @left, @top, @width, @height = line.scan(/\d+/).map(&:to_i)
    @overlaps = false
  end
  def right
    @left + @width
  end
  def bottom
    @top + @height
  end
end

Claims = open('03.in').readlines.map { |l| Claim.new(l) }

counts = Hash.new(0)

Claims.each do |c|
  (c.left...c.right).each do |i|
    (c.top...c.bottom).each do |j|
      counts[[i, j]] += 1
    end
  end
end

puts counts.values.count { |x| x > 1 }

Claims.combination(2) do |a, b|
  a.overlaps = b.overlaps = true if b.left < a.right && a.left < b.right && b.top < a.bottom && a.top < b.bottom
end

puts Claims.find { |c| !c.overlaps }.id
