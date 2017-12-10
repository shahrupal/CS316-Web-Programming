#!/usr/bin/ruby
require 'json'

puts "Content-type: text/html"
puts

#json = File.read('Sports.json')
#object = JSON.parse(json)

file = open('Sports.json')
theContents = file.read
json = JSON.parse(theContents)


#puts "<html><form action="" method="GET">"
#puts "<select name="titlechoice">"

puts "<select>"
json["sport"].each do |list|
	puts "<option>#{list["title"]}</option>"
end
puts "</select>"

