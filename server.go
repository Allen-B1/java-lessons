package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
)

const LESSONS = `
I1 I2 I3 I4 I5 E1
C1 C2
`

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/" {
			w.Header().Set("Location", "/")
			w.WriteHeader(303)
			return
		}

		names := strings.Fields(LESSONS)
		t, err := template.ParseFiles("index.html")
		if err != nil {
			log.Println(err)
			w.WriteHeader(500)
			return
		}
		if err := t.Execute(w, names); err != nil {
			log.Println(err)
		}
	})
	r.HandleFunc("/{lesson}", func(w http.ResponseWriter, r *http.Request) {
		vars := mux.Vars(r)
		body, err := ioutil.ReadFile("out/" + vars["lesson"] + ".html")
		if err != nil {
			fmt.Fprintln(w, err)
		}
		w.Header().Set("Content-Type", "text/html")
		w.Write(body)
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	http.ListenAndServe(":"+port, r)
}
