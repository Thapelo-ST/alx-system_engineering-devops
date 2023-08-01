#!/usr/bin/env ruby

def match_caps(input)
  # insert delim to be found
  pattern = /[A-Z]/

  matches = input.scan(pattern)

  if matches.empty?
    puts ""
  else
    puts "#{matches.join('')}"
  end
end


# validate the arguments
if ARGV.length != 1
  puts "Ussage: ruby file.rb <input text>"
else
  match_caps(ARGV[0])
end
