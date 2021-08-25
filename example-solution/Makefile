# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/23 12:44:12 by jnovotny          #+#    #+#              #
#    Updated: 2021/08/25 21:51:37 by jnovotny         ###   ########.fr        #
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