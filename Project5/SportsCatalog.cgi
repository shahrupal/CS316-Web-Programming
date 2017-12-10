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

# creates drop-down list of titles
puts "<select>"
json["sport"].each do |list|
	puts "<option>#{list["title"]}</option>"
end
puts "</select>"

# creates drop-down list of results
puts "<select>"
json["sport"].each do |list|
	list["results"].each do |results,files|
		puts "<option>#{results}</option>"
	end
end
puts "</select>"

# creates drop-down list of search terms
puts "<select>"
json["sport"].each do |list|
	list["searchterms"].each do |terms|
		puts "<option>#{terms}</option>"
	end
end
puts "</select>"

