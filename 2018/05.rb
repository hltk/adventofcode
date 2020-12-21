Input = open('05.in').readlines[0]

def react(inp)
  stack = []
  inp.chars.each do |c|
    if !stack.empty? && stack[-1].swapcase == c
      stack.pop
    else
      stack << c
    end
  end
  stack.length
end

puts react(Input)

r = ('a'..'z').map { |k| react(Input.gsub(/#{k}/i, '')) }.min
puts r
