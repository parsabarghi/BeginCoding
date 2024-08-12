const body = document.getElementsByTagName("body")[0];

function setColor(name) {
    if (!body.classList.contains('dark-mode')) {
        body.style.backgroundColor = name;
    }
}

function randomColor() {
    if (!body.classList.contains('dark-mode')) {
        const red = Math.round(Math.random() * 255);
        const green = Math.round(Math.random() * 255);
        const blue = Math.round(Math.random() * 255);
        
        const color = `rgb(${red}, ${green}, ${blue})`;
        body.style.backgroundColor = color;
    }
}

function toggleDarkMode() {
    body.classList.toggle('dark-mode');
    if (body.classList.contains('dark-mode')) {
        body.style.backgroundColor = '#333';
    } else {
        body.style.backgroundColor = '#f0f0f0';
    }
}