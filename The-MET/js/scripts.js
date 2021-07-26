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
    console.log(object.accessionYear, object.department, object.objectName, object.title, object.prinaryImageSmall)
    
    const detailSegment =
        `<div>
            <label>Year art was acquired: ${object.accessionYear} </label>
            <br>
            <label>Curatorial department: ${object.department} </label>
            <br>
            <label>Type of object: ${object.objectName} </label>
            <br>
            <label>Date when artwork was designed/created: ${object.objectDate} </label>
            <br>
            <label>Country where artwork was created or found: ${object.country} </label>
            <br>
            <label>Page on metmuseum.org: <a href="${object.objectURL}" target="_blank"> Click here<a>  </label>
        </div>`
        
    document.querySelector('#details').innerHTML = detailSegment;

    const imageDisplay = document.getElementById('image').getContext('2d')
    let objectImage = new Image();
    imageDisplay.drawImage(objectImage, 0, 0)

    objectImage.src = object.primaryImageSmall
    console.log(objectImage.src);

}
