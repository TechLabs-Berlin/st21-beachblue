function initMap() {
  const malaga = {lat: 36.719631, lng: -4.420000};
  const map = new google.maps.Map(
    document.getElementById('map'), {zoom: 9, center: malaga}
  );

  let marker = new google.maps.Marker({position: malaga, map: map}
    );
}

