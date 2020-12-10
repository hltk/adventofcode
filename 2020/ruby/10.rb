require './utils.rb'

a = read('10').ints
a += [a.max + 3] + [0]
a.sort!

diffs = a.each_cons(2).map{|x,y|y - x}.tally
p diffs[1] * diffs[3]

dp = Hash.new 0
dp[0] = 1
a.each{|x|
  dp[x] = (x-3..x).map{|x|dp[x]}.sum
}

p dp[a.last]
