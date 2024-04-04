#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define the regular expression pattern using a repetition to
# match the specified cases
pattern = /hb{2.5}tn/

# Check if the argument matches the regular expression pattern
if argument.match?(pattern)
  puts argument
else
  puts "no match found"
end
