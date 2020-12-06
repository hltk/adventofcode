require './utils.rb'
p read(1).ints.combination(2).find{|s|s.sum==2020}.inject(:*)
p read(1).ints.combination(3).find{|s|s.sum==2020}.inject(:*)
