#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define BUFFER_SIZE 1024
#define TOKEN_DELIM " \t\r\n\a"

int main(int argc, char *argv[]) {
  char *line;
  char **tokens;
  int status;

  do {
    printf("> ");
    line = readline();
    tokens = split_line(line);
    status = execute(tokens);

    free(line);
    free(tokens);
  } while (status);

  return 0;
}

char *readline(void) {
  char *buffer = malloc(sizeof(char) * BUFFER_SIZE);
  int position = 0;
  int c;

  if (!buffer) {
    fprintf(stderr, "Error: Allocation error\n");
    exit(EXIT_FAILURE);
  }

  while (1) {
    c = getchar();

    if (c == EOF || c == '\n') {
      buffer[position] = '\0';
      return buffer;
    } else {
      buffer[position] = c;
    }

    position++;

    if (position >= BUFFER_SIZE) {
      fprintf(stderr, "Error: Line too long\n");
      exit(EXIT_FAILURE);
    }
  }
}

char **split_line(char *line) {
  int position = 0;
  char **tokens = malloc(sizeof(char) * BUFFER_SIZE);
  char *token;

  if (!tokens) {
    fprintf(stderr, "Error: Allocation error\n");
    exit(EXIT_FAILURE);
  }

  token = strtok(line, TOKEN_DELIM);

  while (token != NULL) {
    tokens[position] = token;
    position++;

    if (position >= BUFFER_SIZE) {
      fprintf(stderr, "Error: Too many arguments\n");
      exit(EXIT_FAILURE);
    }

    token = strtok(NULL, TOKEN_DELIM);
  }

  tokens[position] = NULL;
  return tokens;
}

int execute(char **args) {
  pid_t pid;
  int status;

  pid = fork();

  if (pid == 0) {
    if (execvp(args[0], args) == -1) {
      perror("Error");
    }

    exit(EXIT_FAILURE);
  } else if (pid < 0) {
    perror("Error");
  } else {
    do {
      waitpid(pid, &status, WUNTRACED);
    } while (!WIFEXITED(status) && !WIFSIGNALED(status));
  }

  return 1;
}