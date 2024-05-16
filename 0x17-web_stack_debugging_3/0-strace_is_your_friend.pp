# Puppet manifest to replace a line in a file using file_line resource
include stdlib  # Include the stdlib module

# Define the file path
$file_to_edit = '/var/www/html/wp-settings.php'

# Ensure the file_line module is available (if not already installed)
package { 'puppetlabs-stdlib':
  ensure => installed,
}

# Replace the line containing "phpp" with "php"
file_line { 'replace_line_in_wp_settings':
  ensure  => present,               # Ensure is the first attribute
  path    => $file_to_edit,
  line    => 'new_line_to_insert',  # Replace this with the actual line you want to insert
  match   => '^.*phpp.*$',         # Regular expression to match the line containing "phpp"
  require => File[$file_to_edit],  # Ensure the file exists before modifying it
}
