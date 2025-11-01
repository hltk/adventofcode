require 'httparty'
require 'fileutils'

CACHE = ENV['XDG_CACHE_HOME'] || "#{ENV['HOME']}/.cache"
CONFIG = ENV['XDG_CONFIG_HOME'] || "#{ENV['HOME']}/.config"
TOKEN = File.read("#{CONFIG}/aocd/token").strip

def read(day = nil, year = nil)
  day ||= Time.new.day
  year ||= Time.new.year
  path = "#{CACHE}/adventofcode/#{TOKEN}"
  FileUtils.mkdir_p path
  fp = "#{path}/#{day}"
  return File.read(fp) if File.file?(fp)

  url = "https://adventofcode.com/#{year}/day/#{day}/input"
  resp = HTTParty.get(url, { headers: { 'Cookie' => "session=#{TOKEN}" } })
  if resp.code != 200
    puts("error code: #{resp.code}\nbody: #{resp.body}")
    exit
  end
  File.write(fp, resp.body)
  resp.body
end

class String
  def ints
    self.scan(/\d+/).map &:to_i
  end
end
