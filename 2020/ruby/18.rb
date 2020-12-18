require './utils.rb'

class Integer
  def -(oth)
    self * oth
  end
  def /(oth)
    self + oth
  end
end

p read(18).lines.map { |l| eval l.tr('+*', '/-') }.sum
