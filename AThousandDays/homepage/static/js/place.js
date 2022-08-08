async function updatePage() {
    var pk = getNewRandPk();
    let response = await fetch("/place_router/places/" + pk)
        .then((response) => response.json())
        .then((place) => {
            return place;
        });
    // let result_json = response.json().then()
    document.getElementById("title").innerText = response.title;
    document.getElementById("place_pic").src=response.img;
    document.getElementById("address").innerText = "Address: " + response.address;
    document.getElementById("dateStart").innerText = "Date Start: " + response.date_start;
    document.getElementById("dateEnd").innerText = "Date End: " + response.date_end;
    document.getElementById("description").innerText = response.description;
    document.getElementById("pk").innerText = response.pk;
}

function getNewRandPk() {
    var pk = allPks[Math.floor(Math.random() * allPks.length)];
    while (allPks.length != 1 && pk == document.getElementById("pk").innerText) {
        pk = allPks[Math.floor(Math.random() * allPks.length)];
    }
    return pk;
}