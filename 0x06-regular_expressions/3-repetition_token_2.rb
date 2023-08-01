#!/usr/bin/env ruby

def match_school(input)
  # insert delim to be found
  pattern = /^h(b+t+n)/

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
  puts "Ussage: ruby match_school.rb <input text>"
else
  match_school(ARGV[0])
end
