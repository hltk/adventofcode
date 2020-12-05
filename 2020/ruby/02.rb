l = ARGF.map{|l|
  l.match(/(\d+)-(\d+) (.): (\w+)/).captures
}

p l.count{|a,b,c,d| 
  d.count(c).between?(a.to_i, b.to_i)
}

p l.count{|a,b,c,d| 
  (d[a.to_i-1] + d[b.to_i-1]).count(c) == 1
}
