#!/usr/bin/env ruby

# Get the log file path from command line argument
log_file_path = ARGV[0]

# Check if the log file path is provided
if log_file_path.nil?
  puts "Usage: ./100-textme.rb [log_file_path]"
  exit 1
end

# Read the log file
log_contents = File.read(log_file_path)

# Define the regular expression pattern to extract sender,
# receiver, and flags
pattern = /\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/

# Extract sender, receiver, and flags from each log entry and
# format the output
matches = log_contents.scan(pattern)
matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end
