package main

import (
	"encoding/json"
	"io"
	"log"
	"os"
)

// Struct for the JSON formation of the first JSON object (count + seq)
type CountSeq struct {
	Count int `json:"count"`
	Seq []interface{} `json:"seq"`
}


func main() {

	// Read in the < filename
	dec := json.NewDecoder(os.Stdin)

	// JSON Values are interface{} (generic)
	var jsonVals []interface{}

	// Reading through file, taken from
	// https://golang.org/pkg/encoding/json/
	for {
		var blank interface{}
		err := dec.Decode(&blank)
		if err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}
		jsonVals = append(jsonVals, blank)
	}

	/*
	for i := 0; i < len(jsonVals); i++ {
		log.Println(jsonVals[i])
	}*/

	os.Stdout.Write(formCountSeq(jsonVals))
	outputList(formList(reverseJsonValues(jsonVals)))

}

// Takes in the slice of JSON values and returns []byte of
// The result (count + values)
func formCountSeq(jsonValues []interface{}) []byte {

	count := len(jsonValues)

	coSeq := CountSeq{
		Count:      count,
		Seq: jsonValues,
	}

	res, err := json.Marshal(coSeq)

	if err != nil {
		log.Fatal(err)
	}

	return res
}

// Outputs the json values in the slice to stdout
func outputList(jsonValues []interface{})  {
	enc := json.NewEncoder(os.Stdout)
	enc.Encode(jsonValues)
}

// Forms the second JSON object (count, then values in reverse order)
func formList(jsonValues []interface{}) []interface{} {
	var jsonList []interface{}
	jsonList = append(jsonList, len(jsonValues))
	jsonList = append(jsonList, jsonValues...)
	return jsonList
}

// Reverses slice
// https://github.com/golang/go/wiki/SliceTricks#reversing
func reverseJsonValues(jsonValues []interface{}) []interface{} {
	reverse := make([]interface{}, len(jsonValues))
	copy(reverse, jsonValues)
	for left, right := 0, len(reverse) - 1; left < right; left, right = left + 1, right - 1 {
		reverse[left], reverse[right] = reverse[right], reverse[left]
	}
	return reverse
}


















