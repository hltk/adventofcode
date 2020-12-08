require './utils.rb'
l=read(8).split "\n"

it = 0
acc = 0
seen = Set.new

while !seen.include?(it)
  seen.add it
  a, b = l[it].split
  case a
  when 'jmp' then it += b.to_i - 1
  when 'acc' then acc += b.to_i
  end
  it += 1;
end

puts acc

def f i
  l=read(8).split("\n")
  it = 0
  acc = 0
  seen = Set.new
  while 0 <= it && it < l.size
    return if seen.include? it
    seen.add it
    a, b = l[it].split
    if i == it && a != 'acc'
      a = a == 'jmp' ? 'nop' : 'jmp'
    end
    case a
    when 'jmp' then it += b.to_i - 1
    when 'acc' then acc += b.to_i
    end
    it += 1
  end
  puts acc
end

(0...l.size).map{|x|f(x)}
