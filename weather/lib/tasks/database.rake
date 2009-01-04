namespace :db do

  task :create => :merb_env do
    [Resort, Measure, MeasurePoint].each do |model|
      model.create_table!
    end
  end
end
