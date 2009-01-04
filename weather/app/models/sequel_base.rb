class Sequel::Base < Sequel::Model

  def self.next_sequence
    DB.execute("SELECT #{self.table_name}_seq.nextval FROM user_sequences").fetch[0].to_i
  end

  def self.create_table
    DB.execute("CREATE SEQUENCE #{self.table_name}_seq START WITH 1 INCREMENT BY 1 NOMAXVALUE")
    super
  end

  def self.create_table!
    DB.execute("DROP SEQUENCE #{self.table_name}_seq")
    super
  end

end
