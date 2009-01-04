class Sequel::Base < Sequel::Model

  def self.next_sequence
    DB.execute("SELECT #{self.table_name}_seq.nextval FROM user_sequences").fetch[0].to_i
  end

end
