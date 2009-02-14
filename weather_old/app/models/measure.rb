class Measure < Sequel::Base

  set_dataset(dataset.from(name.underscore.pluralize))

  set_schema do
    primary_key :measure_id, :auto_increment => false
    foreign_key :resort_id, :table => :resorts, :null => false
    timestamp   :taken_at, :default => "CURRENT_TIMESTAMP".lit
    integer     :freezing_level
  end

end
