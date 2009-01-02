# Go to http://wiki.merbivore.com/pages/init-rb
 
# Specify a specific version of a dependency
# dependency "RedCloth", "> 3.0"

use_orm :sequel
use_test :rspec
use_template_engine :erb

Merb::Config.use do |c|
  c[:use_mutex] = false
  c[:session_store] = 'cookie'  # can also be 'memory', 'memcache', 'container', 'datamapper

  # cookie session store configuration
  c[:session_secret_key]  = '3dd1dc6d4ce4cfae6c0d1c072bc51656f961dc2f'  # required for cookie session store
  c[:session_id_key] = '_weather_session_id' # cookie session id key, defaults to "_session_id"
end

Merb::BootLoader.before_app_loads do
  # This will get executed after dependencies have been loaded but before your app's classes have loaded.
end

Merb::BootLoader.after_app_loads do
  DB = Sequel::DATABASES.first
  # This will get executed after your app's classes have been loaded.
end
