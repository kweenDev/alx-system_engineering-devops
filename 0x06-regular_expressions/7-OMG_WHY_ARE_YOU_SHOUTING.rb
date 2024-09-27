#!/usr/bin/env ruby

# Get the first command line argument
argument = ARGV[0]

# Define the regular expression pattern to match only capital letters
pattern = /[A-Z]/

# Use scan method to find all capital letters in the argument and
# join them into a single string
shouting = argument.scan(pattern).join

# Print the resulting string of capital letters (shouting)
puts shouting
