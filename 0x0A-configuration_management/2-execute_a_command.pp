# Execution file that kills the process KILLMENOW

exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin',
  onlyif      => '/usr/bin/pgrep killmenow',
  refreshonly => true,
}
