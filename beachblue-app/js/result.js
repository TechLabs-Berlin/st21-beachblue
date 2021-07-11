//function to sort the JSON based on parameter
function sortJSON(arr, key, way) {
  return arr.sort(function(a, b) {
      let x = a[key]; let y = b[key];
      if (way === 'asc') { return ((x < y) ? -1 : ((x > y) ? 1 : 0)); }
      if (way === 'desc') { return ((x > y) ? -1 : ((x < y) ? 1 : 0)); }
  });
}

function cardFill(json_beach){
  document.getElementById('cards-dynamic').remove();
  $(".cards-container").append(`<div id="cards-dynamic"> </div>`);
  for (let i = 0; i < 6; i++) {
    $("#cards-dynamic").append(
      `<div class="result-card" onclick="showDetails()" id = "beach-id-`+ json_beach[i]["Unnamed: 0"]+ `"> 
        <img class="result-card-img" src="./styles/img/beach-id-`+ json_beach[i]["Unnamed: 0"]+ `.jpeg" alt=""> 
        <div class="card-body"> 
            <p class="lake-beach">` + json_beach[i]["Name"] +`</p> 
            <p class="city-country">` + json_beach[i]["Province"] + ", " + json_beach[i]["Community"] + ` </p> 
        </div> 
        <div class="tags"> 
        </div> 
      </div>`
      )
      for (var [key, value] of Object.entries(json_beach[i])) {
        
        if (key == 'Type_of_Sand' && value != ''){
          $("#beach-id-" + json_beach[i]["Unnamed: 0"]).find('.tags').append(`<a class="tag" href="">`+ value +` Sand</a>`)
        }
        if (key == 'Nudism' && value != 'No'){
          if(value == 'Yes'){
            $("#beach-id-" + json_beach[i]["Unnamed: 0"]).find(".tags").append('<a class="tag" href="">Nudist</a>')
          }else{
            $("#beach-id-" + json_beach[i]["Unnamed: 0"]).find('.tags').append(`<a class="tag" href="">`+ value +` Nudist</a>`)
          }
        }
        if (key == 'Toilets' && value != 'No'){
          $("#beach-id-" + json_beach[i]["Unnamed: 0"]).find('.tags').append('<a class="tag" href="">Toilets</a>')
        }
        if (key == 'Surfing_Zone' && value != 'No'){
          $("#beach-id-" + json_beach[i]["Unnamed: 0"]).find('.tags').append('<a class="tag" href="">Surfing area</a>')
        }
        if (key == 'Showers' && value != 'No'){
          $("#beach-id-" + json_beach[i]["Unnamed: 0"]).find('.tags').append('<a class="tag" href="">Showers</a>')
        }
      }
    
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
      json_beach = filterJson(localStorage.getItem("termSearch"))
      json_beach = filterJsonByList(json_beach);
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



function filterJson(term) {
  return json_beach.filter(({Name, Province, Locality}) => {
    return  Name.toLowerCase() === term.toLowerCase() ||
            Province.toLowerCase() === term.toLowerCase() ||
            Locality.toLowerCase() === term.toLowerCase()
  })
}


function verifyFilters(){
  let arrayFilter = {};
  $(":checkbox").each(function(){
    if(this.checked == true){
      arrayFilter.push('no')
    }else{
      arrayFilter.push('nothing')
    }
  } )
  return arrayFilter;
}



function filterJsonByList(json_beach) {

  let field_filter = [];
  $(":checkbox").each(function(){
    if(this.checked == true){
      field_filter.push('no')
    }else{
      field_filter.push('nothing')
    }
  } )


  return json_beach.filter(({Nudism, Surfing_Zone, Showers,Child_Zone,Toilets,Yacht_Club,Footbaths,Parking,Reachable_by_bus,Trashcans}) => {
    return  Nudism.toLowerCase() != field_filter[0] &&
            Surfing_Zone.toLowerCase() != field_filter[1] &&
            Showers.toLowerCase() != field_filter[2] &&
            Child_Zone.toLowerCase() != field_filter[3] &&
            Toilets.toLowerCase() != field_filter[4] &&
            Yacht_Club.toLowerCase() != field_filter[5] &&
            Footbaths.toLowerCase() != field_filter[6] &&
            Parking.toLowerCase() != field_filter[7] &&
            Reachable_by_bus.toLowerCase() != field_filter[8] &&
            Trashcans.toLowerCase() != field_filter[9]
            
  })
  
}

//about-main

$("#about").attr("hidden",true)

function showDetails(){
  if($('#about').is(":visible")){
    $("#about").attr("hidden",true)
  }else{
    $("#about").attr("hidden",false)
  }
}
document.getElementById("search-text").value = localStorage.getItem("termSearch");

$(':checkbox').click(function(){
  fetchJson();
});

$( "#recomendationButton" ).click(function() {
  window.open('top-recommendations.html',"_self");
});
