# Go

## Basics

- exported names start with capital
- `func add(x int, y int) int`
- `var i, j int = 1, 2` or short declaration `k := 3`
- types:
```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```
- `u := uint(f)` convertion
- `const Pi = 3.14`
- `for i := 0; i < 10; i++ {`, `for ; sum < 1000; {`, `for sum < 1000 {`
- `if x < 0 {`, `if v := math.Pow(x, n); v < lim {` short if
- `switch os := runtime.GOOS; os {` `case "darwin":`
- `defer fmt.Println("world")` defer execution until return

## More types

- Pointers
```
var p *int
i := 42
p = &i
fmt.Println(*p) // read i through the pointer p
*p = 21         // set i through the pointer p
```

- Structs
```
type Vertex struct {
	X int
	Y int
}
Vertex{1, 2}
```
- `var a [2]string` array , `primes := [6]int{2, 3, 5, 7, 11, 13}`
- `var s []int = primes[1:4]` slice, `a[low : high]`
- `q := []int{2, 3, 5, 7, 11, 13}` slice literal
- `a := make([]int, 5)  // len(a)=5` use make
- `s = append(s, 0)` append slice
- `for i, v := range pow {`
- `var m map[string]Vertex` maps, `m = make(map[string]Vertex)`
- `func compute(fn func(float64, float64) float64) float64 {` function as values
- `func adder() func(int) int {` can return function

## Methods

- `func (v Vertex) Abs() float64 {`
- `func (v *Vertex) Scale(f float64) {` can modify value, methods often need to modify receiver
- `type Abser interface { Abs() float64 }` interface
- `interface{}` any type
- `s, ok := i.(string)` type assert
- `switch v := i.(type) {` type switch
- `func (e *MyError) Error() string {` error interface

## Generic
```
func Index[T comparable](s []T, x T) int {
	for i, v := range s {
		// v and x are type T, which has the comparable
		// constraint, so we can use == here.
		if v == x {
			return i
		}
	}
	return -1
}
```
- `type List[T any] struct {` Generic type

## Concurrency

- `go f(x, y, z)` goroutine
- Channels
```
func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // send sum to c
}

func main() {
	s := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c // receive from c

	fmt.Println(x, y, x+y)
}
```
- `ch := make(chan int, 100)` buffered channel, only send when buffer is full
- `v, ok := <-ch` check if channel closed
- Select block until case can run, can also use `default`
```
func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}
```
- `sync.Mutex` access variable at a time to avoid conflict
```
// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	mu sync.Mutex
	v  map[string]int
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	c.v[key]++
	c.mu.Unlock()
}
```
