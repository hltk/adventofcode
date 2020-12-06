require 'open-uri'

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


# Circular linked list implemented in pure Ruby, using the Enumerable mixin
class CircularList
  # The Enumerable mixin provides collection classes with several traversal and
  # searching methods, and with the ability to sort. The class must provide a method
  # each, which yields successive members of the collection. If #max, min, or sort
  # is used, the objects in the collection must also implement a meaningful <=>
  # operator, as these methods rely on an ordering between members of the
  # collection.
  include Enumerable

  # `each` function implemented as required by the Enumerable mixin
  def each(&block)
    block or return enum_for(__method__) { size }
    r = @ptr
    yield r
    while r.next != @ptr
      r = r.next
      yield r
    end
  end

  # A helper class used to represent nodes of the circular list.
  # Instances of this class are also used as 'pointers' to
  # elements of the list.
  class Node
    attr_accessor :next, :prev, :value
    def initialize(value)
      @value = value
    end
  end

  attr_accessor :ptr

  # Takes an initial element as a parameter.
  def initialize(initial)
    @ptr = Node.new(initial)
    ptr.next = ptr
    ptr.prev = ptr
    @size = 1
  end

  # Inserts an element after the element pointed
  # by given the iterator.
  # Returns an iterator to the inserted value.
  def insert_after(iterator, element)
    a = Node.new(element)
    a.prev = iterator
    a.next = iterator.next
    a.next.prev = a
    a.prev.next = a
    @size += 1
    @ptr = a
    a
  end

  # Inserts an element before the element pointed
  # by given the iterator.
  # Returns an iterator to the inserted value.
  def insert_before(iterator, element)
    insert_after(iterator.prev, element)
  end

  # Deletes the element the given iterator points to.
  # Returns an iterator to the node that comes
  # after the deleted one.
  def erase(iterator)
    iterator.prev.next = iterator.next
    iterator.next.prev = iterator.prev
    @ptr = iterator.next
    @size -= 1
    @ptr
  end
end


class PriorityQueue
  def initialize
    @heap = [nil]
  end

  def empty?
    @heap.length == 1
  end

  def pop
    @heap[1], @heap[-1] = @heap[-1], @heap[1]
    r = @heap.pop
    push(1)
    r
  end

  def <<(key)
    @heap << key
    pull(@heap.length - 1)
  end

  private

  def push(i)
    while i * 2 < @heap.length
      c = i * 2
      c += 1 if c + 1 < @heap.length && @heap[c + 1] < @heap[c]
      break if @heap[i] <= @heap[c]
      @heap[c], @heap[i] = @heap[i], @heap[c]
      i = c
    end
  end

  def pull(i)
    while i > 1
      break if @heap[i] >= @heap[i / 2]
      @heap[i], @heap[i / 2] = @heap[i / 2], @heap[i]
      i /= 2
    end
  end
end


#class QueueElem
#  attr_reader :node, :dist
#
#  def initialize(node, dist)
#    @node = node
#    @dist = dist
#  end
#
#  include Comparable
#  def <=>(other)
#    @dist <=> other.dist
#  end
#end
#
#def main
#  nodes, edges = gets.split.map(&:to_i)
#  graph = Array.new(nodes) { Array.new }
#  dist = [-1] * nodes
#  visited = [false] * nodes
#  edges.times do
#    a, b, c = gets.split.map(&:to_i)
#    graph[a - 1] << [b - 1, c]
#  end
#  queue = PriorityQueue.new
#  queue << QueueElem.new(0, 0)
#  dist[0] = 0
#  until queue.empty?
#    cur = queue.pop
#    next if visited[cur.node]
#    visited[cur.node] = true
#    graph[cur.node].each do |nxt, weight|
#      next if dist[nxt] != -1 && cur.dist + weight >= dist[nxt]
#      dist[nxt] = cur.dist + weight
#      queue << QueueElem.new(nxt, cur.dist + weight)
#    end
#  end
#  puts dist
#end
#
#main

require 'httparty'
require 'fileutils'

TOKEN=ENV['AOC']

def read day=nil, year = nil
  day = Time.new.day unless day
  year = Time.new.year unless year
  path = "#{ENV['HOME']}/.cache/adventofcode/#{TOKEN}"
  FileUtils.mkdir_p path
  fp = "#{path}/#{day}"
  return File.read(fp) if File.file?(fp)
  url = "https://adventofcode.com/#{year}/day/#{day}/input"
  resp = HTTParty.get(url, { headers: { "Cookie" => "session=#{TOKEN}" } })
  puts("error: #{resp.code}") == nil && exit if resp.code != 200
  File.write(fp, resp.body)
  return resp.body
end

class String
  def ints(n=true); (n ? self.scan(/-?\d+/) : self.scan(/\d+/)).map &:to_i end
end
