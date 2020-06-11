package main

import (
        "fmt"
        "net"
        "net/http"
)

func getipv4 (w http.ResponseWriter, r *http.Request){
        addrs, _ := net.InterfaceAddrs()
        for _, addr := range addrs {
                if ipnet, ok := addr.(*net.IPNet); ok && !ipnet.IP.IsLoopback(){
                        if ipnet.IP.To4() != nil {
                        fmt.Fprintln(w, ipnet.IP.String())
                        break
                        }
                }
        }
}

func main() {
        http.HandleFunc("/hi", getipv4)
        http.ListenAndServe(":9999",nil)
}