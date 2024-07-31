const form = document.getElementById('form');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    getColors();

});

function getColors(){
const query = form.elements.query.value;
    fetch("/palette", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            query: query
        })
    })
    .then((response) => response.json())
    .then(data => {
        const colors = data.colors;
        const container = document.querySelector('.container');
        createColorBoxes(colors, container);
        console.log(data);
    })}

function createColorBoxes(colors, container){
    container.innerHTML = '';
    for(const color of colors){
        const div = document.createElement('div');
        div.classList.add('color');
        div.style.backgroundColor = color;
        div.style.width = `calc(100% / ${colors.length})`;

        div.addEventListener('click', function () {
            navigator.clipboard.writeText(color);
        });

        const span = document.createElement('span');
        span.innerText = color;
        span.style.display = 'none';
        div.appendChild(span);

        // Show the color code when mouse is over the color box
        div.addEventListener('mouseover', function () {
            span.style.display = 'block';
        });

        // Hide the color code when mouse is out of the color box
        div.addEventListener('mouseout', function () {
            span.style.display = 'none';
        });

        container.appendChild(div);
    }
}