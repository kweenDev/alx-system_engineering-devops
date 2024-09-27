#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define the regular expression pattern to match strings starting
# with 'h', ending with 'n', and having any single character in
# between
pattern = /^h.n$/

# Check if the argument matches the regular expression pattern
if argument.match?(pattern)
  puts argument
else
  puts ""
end
