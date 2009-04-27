require 'date'
require 'yaml'


data_directory = "./data/"

files = Dir.new(data_directory).entries

i = 1

files.each do |entry|
  puts entry + "( "+i.to_s+" of "+files.size.to_s+" )"
  if entry.size > 2:
    data = Marshal.load(File.read("./data/"+entry))
    measurement_hashes = Array.new()
    data.each do |data_element|
      data_element.delete_at(0)
      data_element.each do |conditions|
        measure = Hash.new()

        day_and_time = conditions[0].split(" ")
        #puts "Date: " + day_and_time[0] + " " + day_and_time[1]
        measure['date'] = day_and_time[0] + " " + day_and_time[1]

        time_of_day = day_and_time[2].delete("-")
        #puts "Time of day: " + time_of_day
        measure['time of day'] = time_of_day

        clouds = conditions[1].match(/cloud|partcloud|clear|rainshowers|snowshowers|rain|snow/)
        #puts "Clouds: %s" % [clouds[0]]
        measure['clouds'] = clouds[0]

        wind = conditions[2].split(/wind|metric/)[1]
        wind_data = [wind.match(/[A-Z]+/)[0], wind.match(/[0-9]+/)[0]]
        #puts "Wind: %s %s " % [wind_data[0], wind_data[1]]
        measure['wind'] = wind_data[0] + " " + wind_data[1]
        
        #puts "Summary: " + conditions[3]
        measure['summary'] = conditions[3]

        #puts "Snowfall: " + conditions[4].to_s + " mm"
        measure['snowfall'] = conditions[4].to_s

        #puts "Rainfall: " + conditions[5].to_s + " mm"
        measure['rainfall'] = conditions[5].to_s

        #puts "Max temperature: " + conditions[6].to_s + " deg. C"
        measure['max temp'] = conditions[6].to_s

        #puts "Min temperature: " + conditions[7].to_s + " deg. C"
        measure['min temp'] = conditions[7].to_s

        #puts "Wind chill temperature: " + conditions[8].to_s + " deg. C"
        measure['wind chill'] = conditions[8].to_s

        #puts "Freezing level: " + conditions[9].to_s + " m"
        measure['freeze'] = conditions[9].to_s

        #puts

        measurement_hashes.push(measure)
      end
    end
    File.open("./pydata/"+entry+".pydata", 'w+') {|f| f.puts measurement_hashes.to_yaml}
  end
  i+=1
end



