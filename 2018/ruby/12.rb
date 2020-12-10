require './utils.rb'
data = read(12, 2018)

@inp, _, *@rules = data.split "\n"
@inp.gsub!('initial state: ', '')
@rules = @rules.map{|x| x.split ' => '}.to_h

def run t, pad=10**3
  i = '.' * pad + @inp + '.' * pad
  t.times{
    i = ("." * 2 + i).chars.each_cons(5).map{|x|@rules[x.join]}.join
  }
  i.chars.each_with_index.filter{|x,i| x == '#'}.map{|x,i| i-pad}.sum
end

p run 20

t = 198
target = 50000000000

p run(t)+(target-t)*(run(t)-run(t-1))
