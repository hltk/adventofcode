require './utils'

d = read(6, 2021).ints.tally

256.times do
  nd = Hash.new 0
  d.each { |a, b|
    if a == 0
      nd[8] += b
      nd[6] += b
    else
      nd[a - 1] += b
    end
  }
  d = nd
end
p d.map(&:last).sum
