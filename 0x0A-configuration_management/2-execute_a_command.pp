# Task 2
# Execute a command

exec { 'mytest':
  command => '/usr/bin/pkill killmenow',
}