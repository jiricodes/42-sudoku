# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/23 12:44:12 by jnovotny          #+#    #+#              #
#    Updated: 2021/08/24 20:57:04 by jnovotny         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC=gcc
CFLAGS= -Wall -Wextra -Werror
TARGET=rush-1

.PHONY: all re clean fclean build run-example

all: build run-example run-errors unittest

build:
	$(CC) $(CFLAGS) -o $(TARGET) *.c

run-example:
	./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." | cat -e

run-errors:
	@/bin/echo -ne "1) Too many arguments:\t"
	-@./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." "123456789"
	@/bin/echo -ne "2) Not enough arguments:\t"
	-@./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68."
	@/bin/echo -ne "3) Invalid character:\t"
	-@./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......s"
	@/bin/echo -ne "4) 16 clues:\t"
	-@./$(TARGET) "9...7...." "........." ".6..124.." "84...1.9." "5.....8.." "..1......" "...7..6.." "........." "4........"

test:
	make -C ../tests test

unittest:
	make -C ../tests unittest

clean:
	@rm -f *.o
	-@make -C ../tests clean

fclean: clean
	@rm -f $(TARGET)
	-@make -C ../tests fclean

re: fclean all