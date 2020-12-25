require './utils.rb'

rg = Hash.new { |h, k| h[k] = []}
g = Hash.new { |h, k| h[k] = []}

read(7).lines.each do |line|
  a = line.match(/^(.*) bags contain/)[1]
  line.scan(/(\d+) ([a-z ]+) bags?/).each do |cnt, b|
    rg[b] << a
    g[a] << [b, cnt.to_i]
  end
end

p1 = ->(n) {rg[n].map { |x| p1[x]}.inject([n], :|)}
p p1['shiny gold'].size - 1

p2 = ->(n) {1 + g[n].map { |u, c| p2[u] * c}.sum}
p p2['shiny gold'] - 1
