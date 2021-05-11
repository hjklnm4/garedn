<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=qi22xid0au"></script>
<div id="map" style="width:100%;height:100%;"></div>
<meta charset="utf-8">
<script>
var mapOptions = {
    center: new naver.maps.LatLng(35.854721, 128.482413),
    zoom: 16
};
var map = new naver.maps.Map('map', mapOptions);
 
var marker = new naver.maps.Marker({
    position: new naver.maps.LatLng(35.854721, 128.482413),
    title: '계명대출판부\n보산관 105호',
    map: map
});
 
var contentString = [
        '<div style="padding:4px 4px;">',
        '   <div style="font-weight:bold;padding-bottom:3px;">계명대출판부</div>',
        '   <p>보산관 105호<p>',
        '</div>'
    ].join('');
 
var infowindow = new naver.maps.InfoWindow({
    content: contentString
});
 
naver.maps.Event.addListener(marker, "click", function(e) {
    if (infowindow.getMap()) {
        infowindow.close();
    } else {
        infowindow.open(map, marker);
    }
});
 
infowindow.open(map, marker);
</script>

