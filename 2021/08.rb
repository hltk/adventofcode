require './utils'

data = read(8, 2021)

d = data.lines.map { |x| x.split(" | ").last.strip.split }.flatten.map(&:length).tally

p d[2] + d[3] + d[4] + d[7]

H = {
  "acedgfb" => "8",
  "cdfbe" => "5",
  "gcdfa" => "2",
  "fbcad" => "3",
  "dab" => "7",
  "cefabd" => "9",
  "cdfgeb" => "6",
  "eafb" => "4",
  "cagedb" => "0",
  "ab" => "1"
}

zs = (?a..?g).to_a.permutation.map do |perm|
  l = (?a..?g).zip(perm).to_h
  nh = H.map { |a, b|
    a = a.chars.map { |x| l[x] }.sort.join
    [a, b]
  }.to_h
  [nh.keys.sort, nh]
end.to_h

lol = 0

data.lines.map { |x| x.split(" | ").map &:split}.each do |s0, s1|
  s0 = s0.map { |x| x.chars.sort.join }.sort
  s1 = s1.map { |x| x.chars.sort.join }
  o = zs[s0]
  lol += s1.map { |x| o[x] }.join.to_i
end

p lol
