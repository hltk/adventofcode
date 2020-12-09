require './utils.rb'

a = read('9').lines.map &:to_i

p1 = a.each_cons(26).find{|*v,x| !v.combination(2).map(&:sum).include? x}.last
p p1

i, j = (0...a.size).to_a.combination(2).find{|i,j| a[i..j].sum == p1}
p a[i..j].minmax.sum
