class Resort < Sequel::Base

  set_dataset(dataset.from(name.underscore.pluralize))

  set_schema do
    primary_key :resort_id, :auto_increment => false
    varchar     :name, :size => 60
    varchar     :country, :size => 50
  end

  def self.create_table
    DB.execute("CREATE SEQUENCE resorts_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE")
    super
  end

  def self.create_table!
    DB.execute("DROP SEQUENCE resorts_seq")
    super
  end

end
