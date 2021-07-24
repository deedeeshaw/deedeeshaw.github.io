/*!
* Start Bootstrap - Small Business v5.0.2 (https://startbootstrap.com/template/small-business)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-small-business/blob/master/LICENSE)
*/
async function getApi() {
    randomId = Math.floor(Math.random()*4000);
    console.log(randomId);
    let metUrl = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/' + randomId;
    console.log(metUrl);
    try {
        let result = await fetch(metUrl);
        return await result.json()
    }
    catch (error) {
        console.log(error)
    }
}

async function renderApi() {
    console.log('start here')
    let object = await getApi();
    console.log(object.accessionYear, object.department, object.objectName, object.title, object.artistDisplayName)
}
