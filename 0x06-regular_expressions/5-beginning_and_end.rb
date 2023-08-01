#!/usr/bin/env ruby

def match(input)
  # insert delim to be found
  pattern = /^h.n/

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
  match(ARGV[0])
end
