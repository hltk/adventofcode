require './utils.rb'
l=read(8).split "\n"
it = 0
acc = 0
seen = Set.new
while !seen.include?(it)
  seen.add it
  a, b = l[it].split
  case a
  when 'jmp' then it += b.to_i;
  when 'acc' then acc += b.to_i; it += 1;
  when 'nop' then it += 1;
  end
end
puts acc

(0...l.size).each{|i|
  it = 0
  acc = 0
  seen = Set.new
  while !seen.include?(it) && 0 <= it && it < l.size
    seen.add it
    a, b = l[it].split
    if i == it && a != 'acc'
      a = a == 'jmp' ? 'nop' : 'jmp'
    end
    case a
    when 'jmp' then it += b.to_i;
    when 'acc' then acc += b.to_i; it += 1;
    when 'nop' then it += 1;
    end
  end
  puts acc if !seen.include? it
}
