#!/usr/bin/env ruby

# Checks if the argument matches the regular expression pattern
puts ARGV[0].scan(/hb{2,5}tn/).join
