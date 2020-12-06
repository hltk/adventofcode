M = Integer(1e4) + 7

class ModInt
  include Comparable
  def initialize x = 0; @v = ((x%M)+M)%M end
  def * oth; ModInt.new(@v * oth.get % M) end
  def + oth; ModInt.new((@v + oth.get) % M) end
  def - oth; ModInt.new((@v - oth.get + M) % M) end
  def -@; ModInt.new(-@v) end
  def / oth; self * oth.inv end
  def <=> oth; @v <=> oth.get end
  def inv; self.pow(M - 2) end
  def to_s; @v.to_s end
  def to_i; @v end
  alias get to_i
  alias inspect to_s
  def pow b;
    a = self.clone
    r = ModInt.new(1)
    while b > 0
      r = r * a if b % 2 == 1
      a = a * a
      b /= 2
    end
    r
  end
end

# deal with stack    -x + n - 1
# cut N               x - b
# deal with increment x * k

pos = ModInt.new(2019)

ARGF.each{|x|
  if x =~ /stack/
    pos = -pos + ModInt.new(M - 1)
  elsif x =~ /cut/
    k = x.scan(/-?\d+/).first.to_i
    pos -= ModInt.new(k)
  elsif x =~ /inc/
    k = x.scan(/\d+/).first.to_i
    pos *= ModInt.new(k)
  end
}

p pos
