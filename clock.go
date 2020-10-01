package main

import (
	"fmt"
	"time"
)

var now_hour, now_min, now_sec string

func main() {
	for true {
		if time.Now().Hour() > 12 {
			now_hour = fmt.Sprintf("%d", time.Now().Hour()-12)
		} else {
			now_hour = fmt.Sprintf("%d", time.Now().Hour())
		}
		now_min = fmt.Sprintf("%d", time.Now().Minute())
		now_sec = fmt.Sprintf("%d", time.Now().Second())
		if len(now_hour) == 1 {
			now_hour = fmt.Sprintf("%s", "0"+now_hour)
		}
		if len(now_min) == 1 {
			now_min = fmt.Sprintf("%s", "0"+now_min)
		}
		if len(now_sec) == 1 {
			now_sec = fmt.Sprintf("%s", "0"+now_sec)
		}
		now_time := fmt.Sprintf("%s:%s:%s\nktkalpha", now_hour, now_min, now_sec)
		fmt.Println(now_time)
		time.Sleep(100)
		fmt.Println("\n\n\n\n\n\n\n\n")
	}
}
