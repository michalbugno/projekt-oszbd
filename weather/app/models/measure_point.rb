class MeasurePoint < Sequel::Base

  set_dataset(dataset.from(name.underscore.pluralize))

  set_schema do
    primary_key :measure_point_id, :auto_increment => false
    foreign_key :measure_id, :table => :measures, :null => false
    integer     :snow_thickness
    integer     :rainfall
    integer     :snowfall
    integer     :wind_speed
    integer     :max_temp
    integer     :min_temp
    integer     :height
    integer     :wind_direction
  end

end
