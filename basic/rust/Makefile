# Makefile

# Define the Rust compiler
RUSTC = rustc

# Define the source file
SRC = main.rs

# Define the output file
OUT = main

# Define the flags for the Rust compiler
RUSTFLAGS = -O

# Define the command to compile the Rust source code
$(OUT): $(SRC)
    $(RUSTC) $(RUSTFLAGS) -o $(OUT) $(SRC)

# Define the command to clean up the compiled files
clean:
    rm -f $(OUT)