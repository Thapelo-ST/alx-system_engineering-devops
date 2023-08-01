#!/usr/bin/env ruby

def match(input)
  # insert delim to be found
  pattern = /hbt{2,5}n/

  # match using oniguruma lib
  matches = input.scan(pattern)

  if matches.empty?
    puts ""
  else
    puts "#{matches.join('')}"
  end
end


# validate the arguments
if ARGV.length != 1
  puts "Ussage: ruby match.rb <input text>"
else
  match(ARGV[0])
end
