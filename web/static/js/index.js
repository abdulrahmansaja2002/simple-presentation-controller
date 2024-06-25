const left = document.querySelector('.left-btn .left');
const right = document.querySelector('.right-btn .right');

const press = (key) => {
    console.log("Pressed", key);
    fetch(`/${key}`, {
        method: 'POST'
    }).then(response => {
        response.json().then(data => {
            console.log(data);
        })
    }).catch(err => {
        console.log(err);
    });
}

left.addEventListener('click', () => {
    press('left');
});

right.addEventListener('click', () => {
    press('right');
});