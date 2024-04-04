#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Check if the argument matches the regular expression for "School"
if argument.match?(/School/)
  puts argument
else
  puts "No match found"
end
