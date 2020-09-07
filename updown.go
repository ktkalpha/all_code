package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	var RandomInt int = rand.Intn(100) + 1.
	var UserInput int
	var count int = 0.
	for {
		fmt.Print("100 Up Down:")
		fmt.Scanln(&UserInput)
		fmt.Print("\n")
		if UserInput > RandomInt {
			fmt.Println("Down")
			count += 1
			continue
		}
		if UserInput < RandomInt {
			fmt.Println("Up")
			count += 1
			continue
		}
		if UserInput == RandomInt {
			goto end
		}
	}
end:
	fmt.Println(count, "번만에 성공!")
}
