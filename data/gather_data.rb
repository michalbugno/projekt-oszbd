# EXTRACT - TRANSFORM - LOAD
require "rubygems"
require "ruby-debug"
require "nokogiri"
require 'net/http'

def extract_period(node)
  height = node.search("table//td//a.current//.height").text
  match = node.text.match(/periods (\d\d\d\d\-\d\d-\d\d) through (\d\d\d\d-\d\d-\d\d)/)
  date_from = Date.parse(match[1])
  date_to = Date.parse(match[2])
  [height.to_i, date_from, date_to]
end

def extract_days(node)
  ret = []
  node.search("td").each do |n|
    ret << [n.search("b").text, n.search("span").text].join(" ")
  end
  ret
end

def extract_clouds(node)
  node.search("td/img").map { |e| e["alt"] }
end

def extract_wind(node)
  node.search("td/img").map { |e| e["alt"] }
end

def extract_summary(node)
  node.search("td").map { |e| e.text.strip }
end

def extract_snow(node)
  node.search("td").map { |e| e.text.to_i }
end

def extract_rain(node)
  node.search("td").map { |e| e.text.to_i }
end

def extract_max_temp(node)
  node.search("td").map { |e| e.text.to_i }
end

def extract_min_temp(node)
  node.search("td").map { |e| e.text.to_i }
end

def extract_windchill(node)
  node.search("td").map { |e| e.text.to_i }
end

def extract_freezing_level(node)
  node.search("td").map { |e| e.text.to_i }
end

def parse_text(doc)
  forecasts = doc.search("table.forecasts").first.children

  info = extract_period(forecasts[0])
  data = extract_days(forecasts[1])
  data = data.zip(extract_clouds(forecasts[2]))
  data = data.zip(extract_wind(forecasts[3]))
  data = data.zip(extract_summary(forecasts[4]))
  data = data.zip(extract_snow(forecasts[5]))
  data = data.zip(extract_rain(forecasts[6]))
  data = data.zip(extract_max_temp(forecasts[7]))
  data = data.zip(extract_min_temp(forecasts[8]))
  data = data.zip(extract_windchill(forecasts[9]))
  data = data.zip(extract_freezing_level(forecasts[10]))
  data.each { |e| e.flatten! }
  data.unshift(info)
  data
end

def read_network(domain, path)
  gathered = []
  already_parsed = []
  resource = Net::HTTP.new(domain, 80)
  resource.read_timeout = 5
  repeat = true
  while repeat
    begin
      printf("Getting #{domain}#{path}...")
      headers, txt = resource.get(path)
      printf " done."
      printf(" Parsing...")
      doc = Nokogiri::HTML(txt)
      data = parse_text(doc)
      gathered << data
      already_parsed << path
      path = doc.search("table.forecasts/tr")[0].search("td/table//td/a")[0]["href"]
      repeat = false if already_parsed.include?(path)
      puts " done."
    rescue Timeout::Error => e
      puts e.inspect
    rescue Exception => e
      puts e.inspect
      raise e
    end
  end
  gathered
end

def file_from_path(path)
  path.gsub("/", "_").downcase + ".dat"
end

def parse_url(url)
  url = url[7 .. -1] if url.index("http://") == 0
  url = url.split("/")
  domain = url.shift
  path = url.join("/")
  [domain, "/" + path]
end

domain, path = parse_url(ARGV.shift)
stats = read_network(domain, path)
File.open(file_from_path(path), "w") do |f|
  dump = Marshal.dump(stats)
  f.write(dump)
  puts "Wrote #{dump.size} bytes to #{f.path}"
end
