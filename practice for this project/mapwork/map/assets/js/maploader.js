
    $(document).ready(function () {
        $('.sidenav').sidenav();
        $(".dropdown-trigger1").dropdown();
        $(".dropdown-trigger2").dropdown();
      });

    var locationRio = { lat: -22.915, lng: -43.197 };

    function initMap(lpcationRio) {
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 5,
        center: locationRio,
        gestureHandling: 'cooperative'
      });

      var marker = new google.maps.Marker({
        position: locationRio,
        map: map,
        title: 'Hello World!'
      });
    }


    $('#submit').click(() => {
      const latitude = document.getElementById("latitude").value;
      const longitude = document.getElementById("longitude").value;

      locationRio = { lat: parseFloat(latitude), lng: parseFloat(longitude) };
      initMap(locationRio)
    })
  