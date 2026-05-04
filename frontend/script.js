let map = L.map('map').setView([21.0, 73.0], 7);

// Map tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
}).addTo(map);

// Load hotspots from backend
async function loadHotspots() {
  const res = await fetch('http://127.0.0.1:5000/detect', {
    method: 'POST'
  });

  const data = await res.json();

  data.hotspots.forEach(h => {
    L.marker([h.lat, h.lng])
      .addTo(map)
      .bindPopup(`Waste: ${h.waste_type}`);
  });
}
