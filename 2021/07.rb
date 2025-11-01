require './utils'

d = read(7, 2021).ints

p (d.min..d.max).map { |x|
  d.map { |y|
    z = (x - y).abs
    z * (z + 1) / 2
  }.sum
}.min
