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

  # Inserts given element after a given pointer.
  # Returns an iterator to the inserted value.
  def insert(iterator, element)
    a = Node.new(element)
    a.prev = iterator
    a.next = iterator.next
    a.next.prev = a
    a.prev.next = a
    @size += 1
    @ptr = a
    a
  end

  # Deletes the node the given points to.
  # Returns an iterator to the node that comes
  # after the deleted one.
  def erase(iterator)
    iterator.prev.next = iterator.next
    iterator.next.prev = iterator.prev
    @ptr = iterator.next
    @size -= 1
    @ptr.dup
  end
end

Input = open('09.in').read

P, L = Input.scan(/(\d+) players; last marble is worth (\d+) points/)[0].map(&:to_i)

def solve(last)
  circ = CircularList.new(0)
  ptr = circ.ptr

  scores = Hash.new(0)

  (1..last).each do |i|
    if i % 23 == 0
      scores[i % P] += i
      7.times do
        ptr = ptr.prev
      end
      scores[i % P] += ptr.value
      ptr = circ.erase(ptr)
    else
      ptr = ptr.next
      ptr = circ.insert(ptr, i)
    end
  end

  scores.values.max
end

puts solve(L)

puts solve(L * 100)
