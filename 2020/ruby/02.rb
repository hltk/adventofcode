l = ARGF.map{|l|
  a,b,c,d = l.scan /\w+/
  [a.to_i,b.to_i,c,d]
}

p l.count{|a,b,c,d| 
  d.count(c).between?(a, b)
}

p l.count{|a,b,c,d| 
  (d[a-1] == c) != (d[b-1] == c)
}
