<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=qi22xid0au&submodules=geocoder">
 

function searchAddressToCoordinate(address) {
  naver.maps.Service.geocode({
    query: address
  }, function(status, response) {
    if (status === naver.maps.Service.Status.ERROR) {
      if (!address) {
        return alert('Geocode Error, Please check address');
      }
      return alert('Geocode Error, address:' + address);
    }

    if (response.v2.meta.totalCount === 0) {
      return alert('No result.');
    }

    var htmlAddresses = [],
      item = response.v2.addresses[0],
      point = new naver.maps.Point(item.x, item.y);

    if (item.roadAddress) {
      htmlAddresses.push('[도로명 주소] ' + item.roadAddress);
    }

    if (item.jibunAddress) {
      htmlAddresses.push('[지번 주소] ' + item.jibunAddress);
    }

    if (item.englishAddress) {
      htmlAddresses.push('[영문명 주소] ' + item.englishAddress);
    }

    infoWindow.setContent([
      '<div style="padding:10px;min-width:200px;line-height:150%;">',
      '<h4 style="margin-top:5px;">검색 주소 : '+ address +'</h4><br />',
      htmlAddresses.join('<br />'),
      '</div>'
    ].join('\n'));

    map.setCenter(point);
    infoWindow.open(map, point);
  });
}

function initGeocoder() {
  if (!map.isStyleMapReady) {
    return;
  }

  map.addListener('click', function(e) {
    searchCoordinateToAddress(e.coord);
  });

  $('#address').on('keydown', function(e) {
    var keyCode = e.which;

    if (keyCode === 13) { // Enter Key
      searchAddressToCoordinate($('#address').val());
    }
  });

  $('#submit').on('click', function(e) {
    e.preventDefault();

    searchAddressToCoordinate($('#address').val());
  });

  searchAddressToCoordinate('정자동 178-1');
}

naver.maps.onJSContentLoaded = initGeocoder;
naver.maps.Event.once(map, 'init_stylemap', initGeocoder);
</script>
