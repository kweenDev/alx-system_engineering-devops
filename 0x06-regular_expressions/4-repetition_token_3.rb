#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define teh regular expression pattern using a repetition token
# without square brackets to match the specified cases
pattern = /hb{2,}tn/

# Check if the argument matches the regular expression pattern
if argument.match?(pattern)
  puts argument
else
  puts "No match found"
end
