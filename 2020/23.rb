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

require './utils.rb'

inp = read(23)
inp = inp.chomp.chars.map(&:to_i)
cll = CircularList.new(inp[0])

inp += (inp.max+1..10**6).to_a

cur = cll.ptr
inp.drop(1).each{|x| cur = cll.insert_after cur, x }

cur = cur.next
mx = inp.max
h = {}

cll.each{|x| h[x.value] = x }

(1..10**7).each{|i|
  dest = cur.value - 1
  dest = mx if dest == 0
  cur = cur.next
  vals = []
  3.times{
    vals << cur.value
    cur = cll.erase(cur)
  }
  dest = dest == 1 ? mx : dest - 1 while vals.include? dest
  destptr = h[dest]
  vals.each{|x|
    destptr = cll.insert_after(destptr, x)
    h[destptr.value] = destptr
  }
}

cur = cur.next while cur.value != 1
p cur.next.value * cur.next.next.value
