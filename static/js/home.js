//map
var map = L.map('map').setView([-6.12796, 106.1494842], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var homes
var url = '/koorapi/'

fetch(url)
    .then(response => response.json())
    .then(data => koors = data)
    .then(showhomes => showhome())
    .then(centerrhome => centerhome())

function showhome() {
    koors.forEach(koor => {
        pop = L.popup({
            closeOnClick: true
        }).setContent(koor.nama)

        coords = [koor.coordX, koor.coordY]

        marker = L.marker(coords).addTo(map).bindPopup(pop);

        tooltip = L.tooltip({
            permanent: true
        }).setContent(koor.nama)

        marker.bindTooltip(tooltip)
    });
}

hoes = document.querySelectorAll('.koor')

function centerhome(){
    koors.forEach((koor, index )=>{
        hoes[index].addEventListener("mouseover", (event) => {
            map.flyTo([koor.coordX, koor.coordY], 14)
        })
    })
}