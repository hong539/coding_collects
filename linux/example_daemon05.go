package main

import (
    "fmt"
    "os"

    "github.com/sevlyar/go-daemon"
)

func main() {
    cntxt := &daemon.Context{
        PidFileName: "/tmp/test.pid",
        PidFilePerm: 0644,
        LogFileName: "/tmp/test.log",
        LogFilePerm: 0640,
        WorkDir:     "./",
        Umask:       027,
    }

    d, err := cntxt.Reborn()
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(1)
    }
    if d != nil {
        return
    }
    defer cntxt.Release()

    fmt.Println("daemon started")
}