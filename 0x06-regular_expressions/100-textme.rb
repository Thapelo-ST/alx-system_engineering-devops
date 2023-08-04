#!/usr/bin/env ruby

def parse_log_entry(entry)
  pattern = /\[from:([\w\s+:]+)\] \[to:([\w\s+:]+)\] \[flags:([-\d\s+:]+)\]/

  match = entry.match(pattern)

  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]
    "#{sender},#{receiver},#{flags}"
  else
    ""
  end
end

if ARGV.length != 1
  puts "Usage: ruby script_name.rb '<log_entry>'"
else
  log_entry = ARGV[0]
  result = parse_log_entry(log_entry)
  puts result
end
