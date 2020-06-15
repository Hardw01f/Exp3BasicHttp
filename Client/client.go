package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
)

func main() {
	// 指定したURLにGETを発行する
	res, err := http.Get("http://localhost:8080/hi")
	if err != nil {
		log.Fatal(err)
	}

	// GETのレスポンスの取得
	dumpRes, _ := httputil.DumpResponse(res, true)
	fmt.Printf("%s", dumpRes)
}
