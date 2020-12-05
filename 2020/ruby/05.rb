seats = ARGF.map{|line|
  line.tr('FLBR', '0011').to_i 2
}

p seats.max
p (seats.min..seats.max).find{|i| seats.include?(i-1) &&
                                 !seats.include?(i) &&
                                  seats.include?(i+1)
}
