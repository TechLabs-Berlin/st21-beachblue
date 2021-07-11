function initMap() {
  const malaga = {lat: 41.346176, lng: 2.168365};
  const map = new google.maps.Map(
    document.getElementById('map'), {zoom: 9, center: malaga}
  );

  let marker = new google.maps.Marker({position: malaga, map: map}
    );
}

