M = 119315717514047

class ModInt
  include Comparable
  def initialize x; @v = ((x%M)+M)%M end
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

times = 101741582076661

a, b = ModInt.new(1), ModInt.new(0)

ARGF.to_a.reverse_each{|x|
  if x =~ /stack/
    a = -a
    b = -b
    b += ModInt.new(M - 1)
  elsif x =~ /cut/
    k = x.scan(/-?\d+/).first.to_i
    b += ModInt.new k
  elsif x =~ /inc/
    k = x.scan(/\d+/).first.to_i
    a /= ModInt.new(k)
    b /= ModInt.new(k)
  end
}

# x_1 = ax+b
# x_2 = a^2x+ab + b
# x_3 = a^3x     +a^2b + ab + b
# ...

# \sum{i=0}^k a^ib = (1 - a^n) / (1 - a) * b

x = ModInt.new(2020)
p x * a.pow(times) + b * (a.pow(times) - ModInt.new(1)) / (a - ModInt.new(1))
