require 'date'

data = Marshal.load(File.read("data/_resorts_abtenau_hindcasts_2008-12-01_bot.dat"))
data.each do |data_element|
  data_element.delete_at(0)
  data_element.each do |conditions|
    day_and_time = conditions[0].split(" ")
    puts "Date: " + day_and_time[0] + " " + day_and_time[1]
    puts "Time of day: " + day_and_time[2]
    puts "Clouds: " + conditions[1]
    puts "Wind: " + conditions[2].split(/wind|metric/)[1]
    puts "Summary: " + conditions[3]
    puts "Snowfall: " + conditions[4].to_s + " mm"
    puts "Rainfall: " + conditions[5].to_s + " mm"
    puts "Max temperature: " + conditions[6].to_s + " deg. C"
    puts "Min temperature: " + conditions[7].to_s + " deg. C"
    puts "Wind chill temperature: " + conditions[8].to_s + " deg. C"
    puts "Freezing level: " + conditions[9].to_s + " m"
    puts
  end
end

