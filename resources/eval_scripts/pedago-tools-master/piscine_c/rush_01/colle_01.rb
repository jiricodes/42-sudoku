#!/usr/bin/env ruby

require 'colorize'
require 'differ'

$test00_resp = """6 2 3 7 9 1 8 4 5
4 5 8 3 2 6 9 1 7
1 9 7 4 5 8 2 3 6
7 8 9 5 1 2 4 6 3
2 3 4 6 8 7 5 9 1
5 6 1 9 4 3 7 8 2
3 4 6 2 7 9 1 5 8
9 1 2 8 6 5 3 7 4
8 7 5 1 3 4 6 2 9
"""

$test01_resp = """9 5 2 8 3 1 4 6 7
3 1 7 6 2 4 5 8 9
8 4 6 5 9 7 1 2 3
5 2 1 7 6 8 3 9 4
4 8 9 3 5 2 6 7 1
6 7 3 1 4 9 8 5 2
2 9 5 4 1 6 7 3 8
7 6 4 9 8 3 2 1 5
1 3 8 2 7 5 9 4 6
"""

$test02_resp = """3 6 1 4 9 5 8 7 2
5 8 2 7 1 3 9 6 4
7 4 9 6 2 8 3 1 5
9 5 4 1 7 2 6 8 3
6 7 8 5 3 9 4 2 1
2 1 3 8 4 6 5 9 7
8 3 6 2 5 7 1 4 9
1 2 5 9 8 4 7 3 6
4 9 7 3 6 1 2 5 8
"""

$test03_resp = """2 6 4 1 8 7 9 3 5
1 8 9 4 5 3 7 6 2
7 5 3 2 9 6 8 1 4
6 1 7 5 2 9 3 4 8
4 3 8 7 6 1 2 5 9
5 9 2 3 4 8 6 7 1
3 4 6 9 1 2 5 8 7
9 7 5 8 3 4 1 2 6
8 2 1 6 7 5 4 9 3
"""

$test04_resp = """2 6 4 1 8 7 9 3 5
1 8 9 4 5 3 7 6 2
7 5 3 2 9 6 8 1 4
6 1 7 5 2 9 3 4 8
4 3 8 7 6 1 2 5 9
5 9 2 3 4 8 6 7 1
3 4 6 9 1 2 5 8 7
9 7 5 8 3 4 1 2 6
8 2 1 6 7 5 4 9 3
"""

$test05_resp = """9 1 4 3 7 5 2 6 8
2 8 7 4 9 6 1 5 3
3 6 5 8 1 2 4 7 9
8 4 6 5 2 1 3 9 7
5 2 9 6 3 7 8 1 4
7 3 1 9 8 4 5 2 6
1 5 3 7 4 9 6 8 2
6 9 8 2 5 3 7 4 1
4 7 2 1 6 8 9 3 5
"""

def testok
	# Test 00.

	resp = %x[./sudoku "62.....45" ".5.32..1." "...4.8..." "78.5.2.63" "..4.8.5.." "56.9.3.82" "...2.9..." ".1..65.7." "87.....29"]
	if resp == $test00_resp
		puts "Test 00 OK".colorize(:green)
	else
		puts "Test 00 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts $test00_resp
	end


	# Test 01

	resp = %x[./sudoku  "95..31.6." ".1....5.9" ".4.5....." "..1.683.." "........." "..314.8.." ".....6.3." "7.4....1." ".3.27..46"]

	if resp == $test01_resp
		puts "Test 01 OK".colorize(:green)
	else
		puts "Test 01 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts $test01_resp
	end

	# Test 02

	resp = %x[./sudoku  "3..49...." ".82......" "7......15" "..417268." "........." ".138465.." "83......9" "......73." "....61..8"]

	if resp == $test02_resp
		puts "Test 02 OK".colorize(:green)
	else
		puts "Test 02 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts $test02_resp
	end

	# Test 03

	resp = %x[./sudoku  ".6.1..9.." "....5...2" "...2....4" "61.5..3.." ".3..6..5." "..2..8.71" "3....2..." "9...3...." "..1..5.9." ]

	if resp == $test03_resp
		puts "Test 03 OK".colorize(:green)
	else
		puts "Test 03 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts $test03_resp
	end

	# Test 04

	resp = %x[./sudoku  ".1...4..." "...5..9.." "68..1..2." "......48." "578...263" ".24......" ".5..3..96" "..1..6..." "...2...1."]

	if resp == $test04_resp
		puts "Test 04 OK".colorize(:green)
	else
		puts "Test 04 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts $test04_resp
	end
end

def testko

	# Test 00

	resp = %x[./sudoku "9...7...." "2...9..53" ".6..124.." "84...1.9." "5....8.." ".31..4..." "..37..68.." ".9..5.741" "47......." ]

	if resp == "Error\n"
		puts "Test 00 OK".colorize(:green)
	else
		puts "Test 00 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end

	# Test 01

	resp = %x[./sudoku "9...7...." "2...9..53" ".6..624.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "97......."]

	if resp == "Error\n"
		puts "Test 01 OK".colorize(:green)
	else
		puts "Test 01 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end

	# Test 02

	resp = %x[./sudoku "9...7.,.." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "48......."]

	if resp == "Error\n"
		puts "Test 02 OK".colorize(:green)
	else
		puts "Test 02 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end

	# Test 03

	resp = %x[./sudoku "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "........." ".9..5.741"]

	if resp == "Error\n"
		puts "Test 03 OK".colorize(:green)
	else
		puts "Test 03 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end

end

def testspecial
	# Test 00

	resp = %x[./sudoku "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "48......." ]

	if resp == "Error\n"
		puts "Test 00 OK".colorize(:green)
	else
		puts "Test 00 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end

	# Test 01

	resp = %x[./sudoku "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "........." ".9..5.741" "47......."]

	if resp == "Error\n"
		puts "Test 01 OK".colorize(:green)
	else
		puts "Test 01 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end

	# Test 02

	resp = %x[./sudoku  "914375268" "287496153" "365812479" "846521397" "529637814" "731984526" "153749682" "698253741" "472168935"]

	if resp == $test05_resp || resp == ""
		puts "Test 02 OK".colorize(:green)
	else
		puts "Test 02 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts $test02_resp
	end

	# Test 03

	resp = %x[./sudoku "914375268" "287496153" "365812479" "846521397" "529637814" "731984526" "153749682" "698253742" "472168935"]

	if resp == "Error\n"
		puts "Test 03 OK".colorize(:green)
	else
		puts "Test 03 KO".colorize(:red)
		puts "<< ----- Your result"
		puts resp
		puts ">> ----- Expected result"
		puts "Error\n"
	end
end


# ########################################################## #
#		Check for cheating. Use of printf, stdio and commun 		 #
#		function names found on the internet when searching for  #
# 	sudoku resolver algo.	 																	 #
# ########################################################## #

def anti_cheat
	# Check for printf
	resp = %x[grep -rin printf *.c]
	if resp.length > 0
		count = resp.scan(/printf/m).size
		puts "\n/!\\ Found #{count} `printf` functions in the files\n".colorize(:red)
		puts resp
	end

	# Check for stdio
	resp = %x[grep -rin '<stdio.h>' *.c]
	if resp.length > 0
		count = resp.scan(/<stdio.h>/m).size
		puts "\n/!\\ Found #{count} `<stdio.h>` functions in the files\n".colorize(:red)
		puts resp
	end

	# Check for OpenClassroom functions

	openClassroomfun = [
		"estValide",
		"absentSurLigne",
		"absentSurColonne",
		"absentSurBloc",
		"absentDeLigne",
		"absentDeColonne",
		"absentDeBloc",
		"nb_possibles"
	]

	# link = "https://openclassrooms.com/en/courses/1256706-le-backtracking-par-lexemple-resoudre-un-sudoku"

	openClassroomfun.each do |f|
		resp = %x[grep -rin #{f} *.c]
		if resp.length > 0
			puts "\n/!\\ Found `#{f}` functions in the files\n".colorize(:yellow)
			puts resp
		end
	end

	# Check for atomic object functions
	# link = "https://spin.atomicobject.com/2012/06/18/solving-sudoku-in-c-with-recursive-backtracking/"

	funs = [
		"sudokuHelper"
	]

	funs.each do |f|
		resp = %x[grep -rin #{f} *.c]
		if resp.length > 0
			puts "\n/!\\ Found `#{f}` functions in the files\n".colorize(:yellow)
			puts resp
		end
	end

end


def main
	opt = ARGV[0]
	if opt == "-c"
		anti_cheat
	elsif opt == "--testok"
		testok
	elsif opt == "--testko"
		testko
	elsif opt == "--testspecial"
		testspecial
	elsif opt == "--all"
		puts "Passing test OK..."
		testok
		puts "Passing test KO..."
		testko
		puts "Passing special tests"
		testspecial
	end
end
main
