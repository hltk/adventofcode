Grid = ARGF.map &:chomp
N, M = Grid.length, Grid[0].length

def calc(xs,ys)
  (0...N).step(ys).each_with_index.count{|y,x|
    Grid[y][(x*xs) % M] == '#'
  }
end

p calc(3,1)
p [[1,1],[3,1],[5,1],[7,1],[1,2]].map{|a,b| calc(a,b)}.inject :*
