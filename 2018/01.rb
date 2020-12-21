Input = open('01.in').readlines.map(&:to_i)

puts Input.reduce(0, :+)

require 'set'

seen = Set.new
s = 0
i = 0
until seen.member? s
  seen.add s
  s += Input[i % Input.length]
  i += 1
end
puts s
