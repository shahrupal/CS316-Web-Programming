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
combination = false


# searches json file associated with user input for information
def showResults(file,searchterm)

	subfile = open(file)
	subcontents = subfile.read
	subjson = JSON.parse(subcontents)

	# create variables to store win/loss data
	wins = 0
	losses = 0
	total = 0

	# show comments as header
	puts "<h2>"
	subjson["comments"].each do |comments|
		puts "#{comments}"
	end
	puts "</h2>"

	# show game data in table
	puts "<table width=100%>"

	subjson["games"].each do |games|	

		puts "<tr>"
		games.each do |key,value|

			# if user does not specify search terms, no bolding
			if searchterm == "" || key != searchterm
				puts "<td>#{key}:   #{value}</td>"
			# bold search terms
			else
				puts "<td><b>#{key}:   #{value}</b></td>"  
			end

			# count number of wins/losses and total
			if key == "WinorLose"
				if value == "W"
					wins = wins + 1
				else
					losses = losses + 1
				end
				total = total + 1
			end
		end
		puts "</tr>"

	end
	puts "</table>"

	# output summary of wins/losses
	puts "<h3>Games Won: #{wins}  (#{(wins.to_f/total).round(3)*100.0}%)</h3>"
	puts "<h3>Games Lost: #{losses}  (#{(losses.to_f/total).round(3)*100.0}%)</h3>"
	puts "<h3>Total Number of Games: #{total}</h3>"

end



# if user inputs something for title and results, search in json file
if cgi['titlechoice'] != "" && cgi['resultchoice'] != ""
	
	# search for matching title
	json["sport"].each do |list|
		if list["title"] == cgi["titlechoice"]
			
			# search for matching results
			list["results"].each do |results,files|
				if results == cgi["resultchoice"]
				
					# check if json file exists
					if !File.file?(files)
						puts "Error: file does not exist."
					else
						showResults(files,cgi["termchoice"])
					end

					# set valid combination of title and result to be true
					combination = true	
				end					
			end
		
			# if combination is not valid or no json file associated with combination
			if combination == false || files == ""
				puts "Error: this combination does not exist."
			end
	
		end
	end

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
		puts "Result:"
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
		puts "Search Term:"
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
	
		puts "</br>*title and result field are required</br>"

		puts "</center>"

	puts "</form>"

end
puts "</body>"
puts "</html>"
