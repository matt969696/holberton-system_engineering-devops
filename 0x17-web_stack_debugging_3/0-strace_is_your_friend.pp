# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`
exec { 'correction':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  '/bin:/usr/bin:/sbin:/usr/sbin:...'
}