async function updatePage() {
    var pk = getNewRandPk();
    let response = await fetch("/music_router/musics/" + pk)
        .then((response) => response.json())
        .then((music) => {
            return music;
        });
    // let result_json = response.json().then()
    document.getElementById("title").innerText = response.title;
    document.getElementById("music_pic").src=response.img;
    document.getElementById("by").innerText = "By: " + response.by;
    // document.getElementById("date").innerText = "Date: " + response.date;
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