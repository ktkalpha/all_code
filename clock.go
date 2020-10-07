package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func cls() {
	cmd := exec.Command("cmd", "/c", "cls")
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func main() {
	for true {
		if time.Now().Hour() > 12 {
			fmt.Println(fmt.Sprintf("%d:%d", time.Now().Hour()-12, time.Now().Minute()))
		} else {
			fmt.Println(fmt.Sprintf("%d:%d", time.Now().Hour(), time.Now().Minute()))
		}
		time.Sleep(100 * time.Millisecond)
		cls()
	}
}
