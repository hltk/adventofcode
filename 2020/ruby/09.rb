require './utils.rb'

a = read('9').lines.map &:to_i
p1 = nil

prev = a[0...25]
a[25..].each{|x|
  if prev.combination(2).map(&:sum).count(x) == 0
    p1 = x
    break
  end
  prev << x
  prev.shift
}

p p1

(0...a.size).each{|i|
  (i...a.size).each{|j|
    if a[i..j].sum == p1
      p a[i..j].min + a[i..j].max
      exit
    end
  }
}
