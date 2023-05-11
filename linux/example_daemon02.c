#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main()
{
    pid_t pid = fork();
    if (pid < 0) {
        printf("fork failed\n");
        exit(1);
    }
    if (pid > 0) {
        printf("parent process exiting\n");
        exit(0);
    }
    umask(0);
    pid_t sid = setsid();
    if (sid < 0) {
        printf("setsid failed\n");
        exit(1);
    }
    if ((chdir("/")) < 0) {
        printf("chdir failed\n");
        exit(1);
    }
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
    open("/dev/null", O_RDONLY);
    open("/dev/null", O_WRONLY);
    open("/dev/null", O_WRONLY);

    while (1) {
        // write your daemon code here
        sleep(10);
    }

    return 0;
}