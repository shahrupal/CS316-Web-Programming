#!/usr/bin/ruby
require 'json'

puts "Content-type: text/html"
puts

puts "<html>"
puts "<head>"
puts "<title>Sports Catalog</title>"
puts "</head>"
puts "<body>"
puts "<center><h1>Sports Catalog</h1></center>"

file = open('Sports.json')
theContents = file.read
json = JSON.parse(theContents)


puts "<form action=''  method='GET'>"

	puts "<center>"

	# creates drop-down list of titles
	puts "Title:"
	puts "<select name='titlechoice'>"
	json["sport"].each do |list|
		puts "<option>#{list["title"]}</option>"
	end
	puts "</select>"
	puts "</br>"

	# creates drop-down list of results
	puts "Results:"
	puts "<select name='resultchoice'>"
	json["sport"].each do |list|
		list["results"].each do |results,files|
			puts "<option>#{results}</option>"
		end
	end
	puts "</select>"
	puts "</br>"

	# creates drop-down list of search terms
	puts "Search Terms:"
	puts "<select name='termchoice'>"
	json["sport"].each do |list|
		list["searchterms"].each do |terms|
			puts "<option>#{terms}</option>"
		end
	end
	puts "</select>"
	puts "</br>"

	puts "</center>"

puts "</form>"

puts "</body>"
puts "</html>"
