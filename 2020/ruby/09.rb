require './utils.rb'

a = read('9').lines.map &:to_i

p1 = nil
prev = a[0...25]
a[25..].each{|x|
  if prev.combination(2).map(&:sum).count(x) == 0
    p1 = x
    break
  end
  prev = prev[1..] + [x]
}

p p1

(0...a.size).to_a.combination(2).each{|i,j|
  if a[i..j].sum == p1
    p a[i..j].min + a[i..j].max
  end
}
