l = ARGF.map &:to_i

(2..3).each{|n|
  p l.combination(n).find{|s| s.sum == 2020}.inject :*
}
