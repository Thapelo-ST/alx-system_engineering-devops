# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx is running and enabled at boot
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create a custom Nginx configuration file for the 301 redirect
file { '/etc/nginx/sites-available/redirect':
  ensure  => present,
  content => "server {
    listen 80;
    server_name 289867-web-01;

    location /redirect_me {
        return 301 https://www.tradingview.com/;
    }
}",
}

# Enable the custom configuration by creating a symbolic link
file { '/etc/nginx/sites-enabled/redirect':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect',
  require => File['/etc/nginx/sites-available/redirect'],
  notify => Service['nginx'],
}

# Remove the default Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}

# Create a custom index.html with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Ensure Nginx listens on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    server_name _;

    location / {
        root   /var/www/html;
        index  index.html;
    }
}",
  require => File['/var/www/html/index.html'],
  notify => Service['nginx'],
}
