document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([0, 0], 2);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    // Fetch and display fire reports
    fetch('/api/fire-reports/')
        .then(response => response.json())
        .then(reports => {
            reports.forEach(report => {
                L.marker([report.latitude, report.longitude])
                    .addTo(map)
                    .bindPopup(`
                        <strong>Description:</strong> ${report.description || 'No description'}
                    `);
            });
        })
        .catch(error => console.error('Error fetching fire reports:', error));

    // Handle form submission for new fire reports
    const form = document.getElementById('fire-report-form');
    form.addEventListener('submit', event => {
        event.preventDefault();

        // Declare formData inside the form submission handler
        const formData = {
            latitude: document.getElementById('latitude').value,
            longitude: document.getElementById('longitude').value,
            description: document.getElementById('description').value,
        };

        fetch('/api/fire-reports/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer your_access_token', // Include the token here
            },
            body: JSON.stringify({
                latitude: document.getElementById('latitude').value,
                longitude: document.getElementById('longitude').value,
                description: document.getElementById('description').value,
            }),
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Failed to submit fire report');
                }
            })
            .then(data => {
                alert('Fire report submitted successfully!');
                console.log(data);
            })
            .catch(error => {
                alert('Error submitting report: ' + error.message);
                console.error(error);
            });
        
    });
});