require './utils'

data = read(3, 2021)

k = data.split.map(&:chars).transpose

puts k.map { |x|
  x.tally.to_a.max_by(&:last).first
}.join.to_i(2) * k.map { |x|
  x.tally.to_a.min_by(&:last).first
}.join.to_i(2)
