require './utils.rb'

a = read('10').ints
a = [0] + a.sort + [a.max + 3]

diffs = a.each_cons(2).map { |x, y| y - x}.tally
p diffs[1] * diffs[3]

dp = Hash.new 0
dp[0] = 1
a.each  do |x|
  dp[x] = (x - 3..x).map { |x| dp[x]}.sum
end

p dp[a.last]
