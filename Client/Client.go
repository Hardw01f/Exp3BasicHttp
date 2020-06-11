package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
)

func main() {
	url := "http://10.50.0.129:9999/hi"
	req, _ := http.NewRequest("GET", url, nil)
	res, err := http.Head(url)
	res.Header.Set("Hello", "BasicHTTP!")
	if err != nil {
		log.Fatal(err)
	}

	dumpRes, _ := httputil.DumpResponse(res, true)
	fmt.Printf("%s", dumpRes)

	dump, _ := httputil.DumpRequestOut(req, true)
	fmt.Printf("%s", dump)

}