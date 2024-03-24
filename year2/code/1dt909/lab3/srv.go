package main

import (
	"errors"
	"io"
	"log"
	"net/http"
)

// We define a global variable that holds the store
var kvs = make(map[string]string)

// We define an error to indicate that the key is missing
// We do this to be able to identify this error later
var ErrorNoSuchKey = errors.New("no such key")

// Adds a key to the kvs
// error is not used, future improvement
func Post(key string, value string) error {
	kvs[key] = value

	return nil
}

// Fetches a key from the kvs
func Get(key string) (string, error) {
	if value, ok := kvs[key]; ok {
		return value, nil
	} else {
		return "", ErrorNoSuchKey
	}
}

// Deletes a key
// error is not used, future improvement
func Delete(key string) error {
	delete(kvs, key)

	return nil
}

func KVSPost(w http.ResponseWriter, r *http.Request) {
	// We can access the {key} via the request
	key := r.PathValue("key")

	// The value we want to set the key to is in the body
	value, err := io.ReadAll(r.Body)
	defer r.Body.Close()

	// Signal an error, if, e.g., the body was empty
	// We use 500 internal server error and pass
	// the error message from the actual error
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// We can now set the key in the kvs
	// The value is a byte, so we need to convert
	// If the put failed, we again return error 500
	if err = Post(key, string(value)); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// The key is now created, so we return 201
	w.WriteHeader(http.StatusCreated)
}

func Echo(w http.ResponseWriter, r *http.Request) {
	log.Printf("%s, %s, %s\n", r.Method, r.URL, r.PathValue("key"))
	w.WriteHeader(http.StatusOK)
}

func KVSGet(w http.ResponseWriter, r *http.Request) {
	key := r.PathValue("key")

	value, err := Get(key)
	if err != nil {
		if errors.Is(err, ErrorNoSuchKey) {
			http.Error(w, err.Error(), http.StatusNotFound)
		} else {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		return
	}

	w.Write([]byte(value))
}

func KVSDel(w http.ResponseWriter, r *http.Request) {
	key := r.PathValue("key")

	err := Delete(key)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
}

func main() {
	mux := http.NewServeMux()

	// We use the new routing enchancements in Go 1.22
	// "PUT /kvs/{key}" will match any PUT request to /kvs/
	// Whatever follows /kvs/ will be extracted to {kvs} parameter
	// Not that {key} cannot contain, e.g., /
	mux.HandleFunc("POST /kvs/{key}", KVSPost)
	mux.HandleFunc("GET /kvs/{key}", KVSGet)
	mux.HandleFunc("DELETE /kvs/{key}", KVSDel)

	//	srv := &http.Server{
	//		Handler:mux,
	//		Addr:":3000",
	//	}
	http.ListenAndServe(":3000", mux)
	// srv.ListenAndServe()
}
