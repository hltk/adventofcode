require './utils.rb'

a = read('10').ints
a += [a.max + 3] + [0]

diffs = a.sort.each_cons(2).map{|x,y|y - x}.tally
p diffs[1] * diffs[3]

dp = Hash.new{|h,x|
  h[x] = (x-3...x).filter{|i|a.include? i}.map{|i|h[i]}.sum
}
dp[0] = 1
puts dp[a.max + 3]
