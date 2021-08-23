# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/23 12:44:12 by jnovotny          #+#    #+#              #
#    Updated: 2021/08/23 16:21:39 by jnovotny         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC=gcc
CFLAGS= -Wall -Wextra -Werror
TARGET=rush-1

.PHONY: all re clean fclean build run-example

all: build run-example

build:
	$(CC) $(CFLAGS) -o $(TARGET) *.c

run-example:
	./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." | cat -e

run-errors:
	@/bin/echo -ne "1) Too many arguments:\t"
	-@./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." "123456789"
	@/bin/echo -ne "2) Invalid character:\t"
	-@./$(TARGET) "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......s"

clean:
	@rm -f *.o

fclean: clean
	@rm -f $(TARGET)

re: fclean all