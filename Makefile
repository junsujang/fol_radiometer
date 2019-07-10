EXE = radiometer

CC=gcc
CFLAGS=-I.
SRC_DIR = src
IDIR = include
DEPS = $(wildcard $(IDIR)/*.h)
SRC = $(wildcard $(SRC_DIR)/*.c)

radiometermake: $(DEPS)
	$(CC) -fopenmp -lwiringPi -lrt -o $(EXE) $(SRC) $(CFLAGS)

clean:
	$(RM) $(EXE)
