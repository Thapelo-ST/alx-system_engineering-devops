# Puppet manifest to optimize Nginx configuration

# Define an execution resource to fix Nginx configuration
exec { 'optimize-nginx':
  # Use sed to replace worker_processes value in nginx.conf
  command     => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf &&",

  # Restart Nginx service after configuration change
  refreshonly => true,
  subscribe   => Service['nginx'],

  # Set the path for the execution environment
  path        => ['/bin', '/usr/bin', '/usr/sbin'],

  # Add a comment explaining the purpose of this resource
  tag         => 'optimize-nginx',
}

# Define the Nginx service
service { 'nginx':
  # Ensure the service is running
  ensure => running,
}

