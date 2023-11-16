# Puppet manifest to update the limits of holbeton user

# Use sed to replace holberton with foo in limits.conf
exec { 'update-limits-conf':
  command => '/usr/bin/env sed -i s/holberton/foo/ /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
