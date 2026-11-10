require 'setup'
require 'setup/configuration'

# setup-rb 5.999.14 otherwise keeps only the last bound for each gem.
# Keep the complete ranges supplied by %ruby_use_gem_dependency.
if Setup::VERSION == '5.999.14'
  module PreserveGemDependencyBounds
    def use_gem_dependencies=(value)
      if value.is_a?(String)
        value = value.split(/[,;:]/).map(&:strip).reject(&:empty?).each_with_object({}) do |token, dependencies|
          name, requirement = token.split(/\s+/, 2)
          (dependencies[name] ||= []) << requirement
        end
      end
      super(value)
    end
  end
  Setup::Configuration.prepend(PreserveGemDependencyBounds)
end
