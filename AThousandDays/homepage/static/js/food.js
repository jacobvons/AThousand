async function updatePage() {
    var pk = getNewRandPk();
    let response = await fetch("/food_router/foods/" + pk)
        .then((response) => response.json())
        .then((food) => {
            return food;
        });
    // let result_json = response.json().then()
    document.getElementById("title").innerText = response.title;
    document.getElementById("food_pic").src=response.img;
    document.getElementById("by").innerText = "By: " + response.by;
    document.getElementById("date").innerText = "Date: " + response.date;
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