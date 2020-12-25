require './utils.rb'

mem = {}
mask = nil

read.lines.each do |l|
  tokens = l.tr('[=]', '   ').split
  if tokens.size == 2
    mask = tokens.last
  else
    value = tokens.last.to_i
    add = tokens[1].to_i
    add |= mask.tr('X', '0').to_i 2
    add &= ~mask.tr('1X', '01').to_i(2)
    xs = (0...mask.size).find_all { |i| mask[35 - i] == 'X'}
    xs.powerset.each  do |c|
      a = add + c.map { |i| 2**i}.sum
      mem[a] = value
    end
  end
end
p mem.values.sum
