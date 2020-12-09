require './utils.rb'

a = read('9').lines.map &:to_i

p1 = nil
(25...a.size).each{|i|
  if a[i-25...i].combination(2).map(&:sum).count(a[i]) == 0
    p1 = a[i]
    break
  end
}

p p1

(0...a.size).to_a.combination(2).each{|i,j|
  if a[i..j].sum == p1
    p a[i..j].min + a[i..j].max
  end
}
