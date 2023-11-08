class apache_500_error_fix {

  package { 'apache2':
    ensure => 'installed',
  }

  service { 'apache2':
    ensure => 'running',
    enable => true,
    require => Package['apache2'],
  }

  exec { 'get_apache_pid':
    command => 'ps aux | grep apache | grep -v grep | awk \'{print $2}\'',
    path    => '/usr/bin:/bin',
    creates => '/tmp/apache_pid.txt',
  }

  exec { 'strace_apache':
    command     => "sudo strace -p $(cat /tmp/apache_pid.txt) -f -o /tmp/apache_strace.log",
    path        => '/usr/bin:/bin',
    refreshonly => true,
    subscribe   => Exec['get_apache_pid'],
  }

  exec { 'trigger_apache_request':
    command     => 'curl -sI 127.0.0.1',
    path        => '/usr/bin:/bin',
    refreshonly => true,
    subscribe   => Exec['strace_apache'],
    notify      => Exec['fix_apache_error'],
  }

  exec { 'fix_apache_error':
    command => 'echo "Fix the issue here"',
    path    => '/usr/bin:/bin',
    onlyif  => 'grep -q "Internal Service Error" /tmp/apache_strace.log',
    require => [Package['apache2'], Service['apache2']],
  }
}

include apache_500_error_fix

