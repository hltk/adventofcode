require './utils.rb'

M = 119315717514047
times = 101741582076661

a, b = ModInt.new(1), ModInt.new(0)

read(22,2019).lines.reverse_each{|x|
  case x
  when /stack/ then a,b=-a,-b+ModInt.new(M-1)
  when /cut (.*)/ then b+=ModInt.new($1.to_i)
  when /increment (.*)/ then a/= m=ModInt.new($1.to_i); b /= m
  end
}

# x_1 = ax+b
# x_2 = a^2x+ab + b
# x_3 = a^3x     +a^2b + ab + b
# ...
# \sum{i=0}^k a^ib = (1 - a^n) / (1 - a) * b

pos = ModInt.new(2020)
one = ModInt.new(1)
p pos * a.pow(times) + b * (a.pow(times) - one) / (a - one)
