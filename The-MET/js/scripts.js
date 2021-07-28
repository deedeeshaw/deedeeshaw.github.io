/*!
* Start Bootstrap - Small Business v5.0.2 (https://startbootstrap.com/template/small-business)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-small-business/blob/master/LICENSE)
*/
async function getApi() {
    randomId = Math.floor(Math.random()*4000);
    let metUrl = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/' + randomId;
    try {
        let result = await fetch(metUrl);
        return await result.json()
    }
    catch (error) {
        console.log(error)
    }
}

async function renderApi() {
    let object = await getApi();
    console.log(object.accessionYear, object.department, object.objectName, object.title, object.primaryImageSmall)
    
    const detailSegment =
        `<div>
            <label>Year art was acquired: <strong>${object.accessionYear} </strong> </label>
            <br>
            <label>Curatorial department: <strong>${object.department}</strong> </label>
            <br>
            <label>Type of object: <strong>${object.objectName}</strong> </label>
            <br>
            <label>Date when artwork was designed/created: <strong>${object.objectDate} </strong></label>
            <br>
            <label>Country where artwork was created or found: <strong>${object.country}</strong> </label>
            <br>
            <label>Page on metmuseum.org: <a href="${object.objectURL}" target="_blank"> Click here<a>  </label>
        </div>`
        
    document.querySelector('#details').innerHTML = detailSegment;

    const imgSrc = object.primaryImageSmall
    console.log(imgSrc)
    await loadImage(imgSrc);
}

function copyCanvas(img) {
    var canvas = document.getElementById('image');
    var ctx = canvas.getContext('2d');
    canvas.width = img.naturalWidth
    canvas.height = img.naturalHeight
    ctx.drawImage(img, 0, 0);
}

function loadImage(imgSrc) {
    var img = new Image();
    img.onload = function () {
        copyCanvas(img);
    };
    img.src = imgSrc;
}

