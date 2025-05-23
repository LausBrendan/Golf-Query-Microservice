# Golf Quote Generator Microservice

Welcome to the Golf Quote Generator! This microservice provides golf quotes on request, with options to filter by golfer or keyword.

---

## Communication Contract

* Input Format: HTTP GET requests with query parameters
* Output Format: JSON
* Protocol: HTTP
* Response Time: Quotes are returned instantly, though the server is ran locally for this example
* Stability: Once deployed, the quote format and filtering keys will not change

---

## How to REQUEST Data

Send a GET request to the microservice with one of the following patterns:

### Random Quote


GET /quote


### Filter by Golfer Name


GET /quote?golfer=Tiger%20Woods


### Filter by Keyword


GET /quote?keyword=dream

### Example using fetch in JavaScript


fetch("http://localhost:8000/quote?golfer=Tiger%20Woods")
  .then(res => res.json())
  .then(data => console.log(data.quote));

## How to RECEIVE Data

Responses will be returned as JSON objects containing a single quote. If no match is found, a default message is returned.

### Example Successful Response:

{
  "quote": "Tiger Woods: I get to play golf for a living. What more can you ask for, getting paid for doing what you love."
}

### Example No Match:

{
  "quote": "No matching quotes found."
}


## UML Sequence Diagram


![UML sequence diagram](<UML sequence diagram.png>)


## Setup Process

* Run using `python3 -m http.server`
* Ensure `golf_quotes.json` is in the same directory
* You may build your own frontend or other application to call the service, the current method was only made to provide a basic frontend to the microservice.

