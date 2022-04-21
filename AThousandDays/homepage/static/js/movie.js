async function updatePage() {
    var pk = getNewRandPk();
    let response = await fetch("/movie_router/movies/" + pk)
        .then((response) => response.json())
        .then((movie) => {
            return movie;
        });
    // let result_json = response.json().then()
    document.getElementById("title").innerText = response.title;
    document.getElementById("movie_pic").src=response.img;
    document.getElementById("date").innerText = "Date: " + response.date;
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