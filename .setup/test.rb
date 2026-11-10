ENV['RACK_ENV'] = 'test'
if (check_gem_home = ENV['ALT_CHECK_GEM_HOME'])
  Gem.use_paths(Gem.dir, [check_gem_home, *Gem.path])
  ENV['GEM_PATH'] = Gem.path.join(File::PATH_SEPARATOR)
end
require 'bundler/setup'
$LOAD_PATH.unshift(File.expand_path('lib'), File.expand_path('modules'),
                   File.expand_path('test'), Dir.pwd)
tests = Dir['test/**/*_test.rb'].sort
tests.reject! { |file| file.start_with?('test/dhcp_ms_native/') } unless Gem.win_platform?
puts "Running #{tests.length} upstream test files (#{RUBY_PLATFORM})"
tests.each { |file| require File.expand_path(file) }
