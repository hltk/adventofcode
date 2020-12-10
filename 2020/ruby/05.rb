require './utils.rb'
s = read(5).lines.map{|line|line.tr('FLBR', '0011').to_i 2}

p s.max
p (s.min..s.max).find{|i| s.include?(i-1) && !s.include?(i) && s.include?(i+1)}
