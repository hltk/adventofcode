require './utils.rb'

def run
  l = read(DAY).split("\n")
  it = 0
  acc = 0
  while 0 <= it && it < l.size
    a, b = l[it].split
    case a
    when 'jmp' then it += b.to_i - 1
    when 'acc' then acc += b.to_i
    end
    it += 1
  end
  puts acc
end
