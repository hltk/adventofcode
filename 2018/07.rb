Input = open('07.in').readlines

g = Hash.new { |h, k| h[k] = [] }

Input.each do |l|
  a, b = l.scan(/^Step (.) must be finished before step (.) can begin\.$/).first
  g[b] << a
end

todo = g.to_a.flatten.uniq.sort

r = ''

until todo.empty?
  a = todo.filter { |x| g[x].empty? }.first
  r += a
  todo.delete(a)
  g.each do |_, adj|
    adj.delete(a)
  end
end

puts r

Input.each do |l|
  a, b = l.scan(/^Step (.) must be finished before step (.) can begin\.$/).first
  g[b] << a
end

todo = g.to_a.flatten.uniq.sort

workers = {}

t = -1

while todo.any? || workers.any?
  t += 1
  workers.keys.each do |x|
    workers[x] -= 1
    next unless workers[x].zero?
    g.each do |_, adj|
      adj.delete(x)
    end
    workers.delete(x)
  end
  while workers.length < 5
    jobs = todo.filter { |x| g[x].empty? }
    break if jobs.empty?
    a = jobs.first
    todo.delete(a)
    job_length = a.ord - 'A'.ord + 1 + 60
    workers[a] = job_length
  end
end

puts t
