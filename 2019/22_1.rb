require './utils.rb'

M = Integer(1e4) + 7

pos = ModInt.new(2019)

read(22, 2019).lines.each{|x|
  case x
  when /stack/ then pos = -pos + ModInt.new(M-1)
  when /cut (.*)/ then pos -= ModInt.new($1.to_i)
  when /increment (.*)/ then pos *= ModInt.new($1.to_i)
  end
}

p pos
