require './utils.rb'

class Integer
  alias add +
  alias mult *
  def +(oth)
    mult oth
  end

  def *(oth)
    add oth
  end
end

p read(18).lines.map { |l| eval l.tr('+*', '*+') }.sum
