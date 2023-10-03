# make a class for configuring Nginx and custom HTTP header
class nginx_custom_header {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/etc/nginx/sites-available/custom_header':
    ensure  => 'file',
    content => template('nginx_custom_header/custom_header.erb'),
  }

  file { '/etc/nginx/sites-enabled/custom_header':
    ensure => 'link',
    target => '/etc/nginx/sites-available/custom_header',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => [File['/etc/nginx/sites-available/custom_header'], Package['nginx']],
  }
}

# applying the class
include nginx_custom_header
