#!/usr/bin/ruby
require 'cgi'
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

cgi = CGI.new

if cgi['titlechoice'] != "" && cgi['resultchoice'] != ""
	puts "ayeeeee"

	# puts "#{cgi['titlechoice']}" <-- prints out

else

	puts "<form action=''  method='GET'>"

		puts "<center>"

		# creates drop-down list of titles
		puts "Title:"
		puts "<select name='titlechoice'>"
		puts "<option></option>"
		json["sport"].each do |list|
			puts "<option>#{list["title"]}</option>"
		end
		puts "</select>"
		puts "</br>"

		# creates drop-down list of results
		puts "Results:"
		puts "<select name='resultchoice'>"
		puts "<option></option>"
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
		puts "<option></option>"
		json["sport"].each do |list|
			list["searchterms"].each do |terms|
				puts "<option>#{terms}</option>"
			end
		end
		puts "</select>"
		puts "</br>"

		# creates submit button
		puts "<input type='submit' value='submit'>"

		puts "</center>"

	puts "</form>"
end
puts "</body>"
puts "</html>"
