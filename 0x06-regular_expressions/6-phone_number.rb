#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define the regular expression pattern to match 10-digit
# phone number
pattern = /^\d{10}$/

# Check if the argument matches the regular expression pattern
if argument.match?(pattern)
  puts argument
else
  puts ""
end
