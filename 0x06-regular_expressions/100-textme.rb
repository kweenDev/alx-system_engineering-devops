#!/usr/bin/env ruby

# Defines the regular expression pattern to extract sender,
# receiver, and flags
puts ARGV[0].scan(/\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/).join(',')
