# a fuller example, including permissions and ownership
file {'/tmp/school':
  ensure => 'directory',
  owner => 'www-data',
  group => 'www-data'
  mode => '0744',
  content => 'I love Puppet',
}
