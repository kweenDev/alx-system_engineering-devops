#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define the regular expression pattern using a repetition
# token to match the specified cases
pattern = /hb{0}tn/

# Check if the argument matches the regular expression pattern
if argument.match?(pattern)
  puts argument
else
  puts "No match found"
end
