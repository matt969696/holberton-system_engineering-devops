# Tentative to write a correct Puppet manifest

package {'nginx':
  ensure => present,
  name   => 'nginx',
}

file {'/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School\n',
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => [File_line['redirect_me'], File_line['add_header']],
}