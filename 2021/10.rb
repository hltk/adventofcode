require './utils'

d = read(10, 2021).split "\n"

o = "([{<"
c = ")]}>"
s = 0
score = [3, 57, 1197, 25137]
scores = []

d.each do |l|
  loop do
    orig = l.dup
    l.gsub! /(\(\))|(\[\])|(\{\})|(<>)/, ''
    break if l == orig
  end
  corr = false
  l.chars.zip(l[1..].chars).each do |a, b|
    if a and b and o.include? a and c.include? b
      corr = true
      s += score[c.index b]
      break
    end
  end
  next if corr
  x = 0
  l.chars.reverse.each do |a|
    x = 5 * x + o.index(a) + 1
  end
  scores << x
end

p s
p scores.sort[scores.length / 2]
