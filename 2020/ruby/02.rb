require './utils.rb'
l = read(2).lines.map{|l|[*l.ints(false),*l.scan(/[a-z]+/)]}
p l.count{|a,b,c,d|d.count(c).between?(a, b)}
p l.count{|a,b,c,d|(d[a-1] != c) != (d[b-1] != c)}
