a=ARGF.read.split "\n\n"
p a.map{|x|x.split.join.chars.uniq.size}.sum
p a.map{|x|x.lines.map{|y|y.chomp.chars.uniq}.inject(:&).size}.sum
