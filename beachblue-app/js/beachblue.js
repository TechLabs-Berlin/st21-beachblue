
//function to sort the JSON based on parameter
function sortJSON(arr, key, way) {
  return arr.sort(function(a, b) {
      let x = a[key]; let y = b[key];
      if (way === 'asc') { return ((x < y) ? -1 : ((x > y) ? 1 : 0)); }
      if (way === 'desc') { return ((x > y) ? -1 : ((x < y) ? 1 : 0)); }
  });
}

function cardFill(json_beach){
  for (let i = 0; i < 3; i++) {
  document.getElementById("card-" + (i+1)).getElementsByClassName("city-country")[0].textContent = json_beach[i]["Province"] + ", " + json_beach[i]["Community"]
  document.getElementById("card-" + (i+1)).getElementsByClassName("lake-beach")[0].textContent = json_beach[i]["Name"]
  document.getElementById("card-" + (i+1)).getElementsByClassName("description")[0].textContent = json_beach[i]["Descripci"].substring(0,75) + "..."
  document.getElementById("card-" + (i+1)).getElementsByClassName("image")[0].src =  "./styles/img/beach-"+ json_beach[i]["Unnamed: 0"] + ".jpeg";
  }
}

// fetch the new_playas.json file and create a variabe called json_beach
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
      cardFill(json_beach)
      return json_beach
    })
    .catch(function () {
      this.dataError = true;
    })
    //return json_beach
  }

fetchJson();

function storeTerm(){
  localStorage.setItem("termSearch",document.getElementById("search-text").value);
}

$( "#recomendationButton" ).click(function() {
  window.open('top-recommendations.html',"_self");
});

$( "#recomendationButton1" ).click(function() {
  window.open('top-recommendations.html',"_self");
});