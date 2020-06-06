package main

import (
	"fmt"
	"net"
	"net/http"
	"os"
	"strings"
)

// API "/hi"のときに呼ばれる関数
func handleHi(w http.ResponseWriter, req *http.Request) {
	// header

	// 送られてきたHTTPリクエストメソッドを取得
	method := req.Method
	fmt.Println("Get GETRequest!")
	fmt.Println("[method]" + method)

	// HTTPリクエストヘッダの取得
	for key, value := range req.Header {
		fmt.Print("[header]" + key)
		fmt.Println(": " + strings.Join(value, ","))
	}
	fmt.Print("\n")

	// GET
	if method == "GET" {

		// ヘッダの追加
		w.Header().Set("Hello", "BasicHTTP!")

		// IPアドレスの取得
		hostname, err := os.Hostname()
		if err != nil {
			fmt.Printf("hostnameが取れません: %v\n", err)
			return
		}

		addrs, err := net.LookupIP(hostname)
		if err != nil {
			fmt.Printf("IPが取れません: %v\n", err)
			return
		}

		for _, a := range addrs {
			// Fprintで書き込み先を明示的に指定
			fmt.Fprint(w, a)
		}

	}
}

func main() {
	// API(URL)によって呼び出す関数を決める。ルーティング的な？
	http.HandleFunc("/hi", handleHi)
	fmt.Println("Server start!")
	// ポートの指定とサーバの起動
	http.ListenAndServe(":8080", nil)
}
