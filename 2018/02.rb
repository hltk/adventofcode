Input = open('02.in').readlines.map(&:chomp)

def count(n)
  Input.count do |s|
    s.chars.uniq.map { |c| s.count c }.include? n
  end
end

puts count(2) * count(3)

Input.combination(2).each do |a, b|
  common = a.chars.zip(b.chars).select { |x, y| x == y }.map(&:first).join
  puts common if common.length == a.length - 1
end
