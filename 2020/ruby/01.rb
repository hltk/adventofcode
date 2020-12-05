l = ARGF.map &:to_i

p l.combination(2).filter{|s| s.sum == 2020}.first.reduce(1, :*)
p l.combination(3).filter{|s| s.sum == 2020}.first.reduce(1, :*)
