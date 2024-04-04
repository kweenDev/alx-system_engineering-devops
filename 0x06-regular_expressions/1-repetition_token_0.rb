#!/usr/bin/env ruby

# Checks if the argument matches the regular expression pattern
puts ARGV[0].scan(/hbt{2,5}n/).join
