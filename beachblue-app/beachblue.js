
  function fetchJson(){
    fetch('/playas_rating.json')
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP error " + response.status);
      }
      console.log(response.json);
      return response.json();
    })
    .then(json => {
      this.users = json;
      json_beach = this.users
      json_beach = sortJSON(json_beach,'ratings_2','desc')
      console.log("vai retornar o json")
      return json_beach
    })
    .catch(function () {
      this.dataError = true;
    })
  }
// fetch the new_playas.json file and create a variabe called json_beach


//function to sort the JSON based on parameter
      function sortJSON(arr, key, way) {
        return arr.sort(function(a, b) {
            let x = a[key]; let y = b[key];
            if (way === 'asc') { return ((x < y) ? -1 : ((x > y) ? 1 : 0)); }
            if (way === 'desc') { return ((x > y) ? -1 : ((x < y) ? 1 : 0)); }
        });
      }

function cardFill(json_beach){
  document.getElementById("card-1").getElementsByClassName("city-country")[0].textContent = json_beach[0]["Province"] + ", " + json_beach[0]["Community"]
  document.getElementById("card-1").getElementsByClassName("lake-beach")[0].textContent = json_beach[0]["Name"]
  document.getElementById("card-1").getElementsByClassName("description")[0].textContent = json_beach[0]["Descripci"].substring(0,75) + "..."
  document.getElementById("card-1").getElementsByClassName("image")[0].src =  "./styles/img/beach-"+ json_beach[0]["Unnamed: 0"] + ".jpeg";
  
}
let test = fetchJson();
console.log(fetch('/playas_rating.json'))