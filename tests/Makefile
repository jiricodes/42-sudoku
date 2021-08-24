# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/24 11:46:53 by jnovotny          #+#    #+#              #
#    Updated: 2021/08/24 18:44:55 by jnovotny         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

TARGET=example_unittest

SUDOKU?=../example-solution/rush-1

CC=gcc

CFLAGS= -I../example-solution

SRCS=../example-solution/utils_static_grid.c \
	 example-unittest.c \

TEST_OUT_DIR=outputs

.PHONY: all test build unittest clean fclean re

all: test

build: 
	@$(CC) $(CFLAGS) -o $(TARGET) $(SRCS)

unittest: build
	./$(TARGET)

test:
	@mkdir -p $(TEST_OUT_DIR)
	./scripts/test_files.sh $(SUDOKU)

clean:
	@rm -f *.o
	@rm -r $(TEST_OUT_DIR)

fclean:
	@rm -f $(TARGET)

