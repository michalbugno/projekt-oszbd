class Resort < Sequel::Base

  set_dataset(dataset.from(name.underscore.pluralize))

  set_schema do
    primary_key  :resort_id, :auto_increment => false
    varchar      :name, :size => 60
    varchar      :country, :size => 50
    sdo_geometry :location
  end

end
