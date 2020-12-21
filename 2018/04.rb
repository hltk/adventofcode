class Guard
  attr_reader :id, :asleep

  def initialize(id)
    @id = id
    @asleep = Hash.new(0)
  end

  def nap!(f, t)
    (f...t).each do |x|
      @asleep[x] += 1
    end
  end

  def fminute
    @asleep.max_by { |_k, v| v }
  end
end

guards = Hash.new { |h, k| h[k] = Guard.new(k) }

id = nil
f = nil

open('04.in').readlines.sort.each do |l|
  if l =~ /Guard #(\d+)/
    id = Regexp.last_match[1].to_i
  elsif l =~ /(\d\d)\] falls asleep/
    f = Regexp.last_match[1].to_i
  elsif l =~ /(\d\d)\] wakes up/
    guards[id].nap!(f, Regexp.last_match[1].to_i)
  end
end

guards = guards.values

r = guards.max { |a, b| a.asleep.values.sum <=> b.asleep.values.sum }

puts r.id * r.fminute.first

r = guards.max { |a, b| a.fminute.last <=> b.fminute.last }

puts r.id * r.fminute.first
