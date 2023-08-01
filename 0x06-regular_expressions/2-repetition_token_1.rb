#!/usr/bin/env ruby

def match(input)
  # insert delim to be found
  pattern = /^h(b{0,1})tn/

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
  puts "Ussage: ruby file <input text>"
else
  match(ARGV[0])
end
