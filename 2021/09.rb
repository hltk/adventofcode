require './utils'

g = read(9, 2021).split "\n"

n, m = g.length, g[0].length

@g = g
@seen = Set.new
@n = n
@m = m

def dfs i, j
  return 0 if @g[i][j] == "9"
  return 0 if @seen.include?([i, j])
  @seen << [i, j]
  s = 1
  s += dfs(i + 1, j) if i + 1 < @n and @g[i + 1][j] > @g[i][j]
  s += dfs(i, j + 1) if j + 1 < @m and @g[i][j + 1] > @g[i][j]
  s += dfs(i - 1, j) if i > 0 and @g[i - 1][j] > @g[i][j];
  s += dfs(i, j - 1) if j > 0 and @g[i][j - 1] > @g[i][j]
  return s
end

lol = []

(0...n).to_a.product((0...m).to_a) do |i, j|
  next if i > 0 and g[i - 1][j] <= g[i][j]
  next if j > 0 and g[i][j - 1] <= g[i][j]
  next if i + 1 < n and g[i + 1][j] <= g[i][j]
  next if j + 1 < m and g[i][j + 1] <= g[i][j]
  lol << dfs(i, j)
end

p lol.sort.reverse[..2].inject :*
