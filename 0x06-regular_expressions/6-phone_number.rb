#!/usr/bin/env ruby

def match_phone_no(input)
  # insert delim to be found
  pattern = /^\d{10}/

  # check if its a real number
  if input =~ pattern
    puts "#{input}"
  else
    puts ""
  end
end


# validate the arguments
if ARGV.length != 1
  puts "Ussage: ruby file.rb <input text>"
else
  match_phone_no(ARGV[0])
end
