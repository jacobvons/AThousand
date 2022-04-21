async function updatePage() {
    var pk = getNewRandPk();
    let response = await fetch("/photo_router/photos/" + pk)
        .then((response) => response.json())
        .then((photo) => {
            return photo;
        });
    // let result_json = response.json().then()
    document.getElementById("title").innerText = response.title;
    document.getElementById("photo_pic").src=response.img;
    document.getElementById("by").innerText = "By: " + response.by;
    document.getElementById("description").innerText = response.description;
    document.getElementById("pk").innerText = response.pk;
}

function getNewRandPk() {
    var pk = allPks[Math.floor(Math.random() * allPks.length)];
    while (appPks.length != 1 && pk == document.getElementById("pk").innerText) {
        pk = allPks[Math.floor(Math.random() * allPks.length)];
    }
    return pk;
}