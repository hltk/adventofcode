require './utils'

d = read(12, 2021).split("\n").map { |x| x.split "-" }
d += d.map &:reverse
d = d.group_by(&:first).transform_values { |x| x.map &:last }

def search(a, b, o, s, d)
  return 1 if a == b
  r = 0
  d[a].each { |x|
    next if x == "start"
    if x[0] == x[0].upcase or !o or !s.include? x
      r += search(x, b, o || (x[0] != x[0].upcase && s.include?(x)), s + [x], d)
    end
  }
  r
end

p search("start", "end", false, ["start"], d)
