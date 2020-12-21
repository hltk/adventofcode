class Node
  attr_reader :sum, :value

  def initialize(str)
    c, m = 2.times.collect { str.next }
    children = c.times.collect { Node.new(str) }
    metadata = m.times.collect { str.next }
    if c.zero?
      @value = metadata.sum
    else
      @value = metadata.map { |x| children[x - 1] }.compact.map(&:value).sum
    end
    @sum = metadata.sum + children.map(&:sum).sum
  end
end

Input = open('08.in').readlines[0].split.map(&:to_i)

root = Node.new(Input.each)

puts root.sum

puts root.value
