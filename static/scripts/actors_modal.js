function actorsModal () {
    let actors_button = document.getElementsByClassName('name')

    for (let actor_button of actors_button) {
        let url = actor_button.getAttribute('actor_url')
        let movies_table = document.getElementsByClassName('modal-body')[0]

        actor_button.addEventListener("click", e => {

            while (movies_table.firstChild) {
            movies_table.removeChild(movies_table.firstChild)
            }
            fetch(url)
                .then((response) => {
                    return response.json()
                })
                .then((movies) => {
                    console.log(movies)
                    for (let movie of movies) {
                        console.log(movie)
                        let newModalRow = movies_table.insertRow(-1)

                        for (let key in movie) {
                            let newModalCell = newModalRow.insertCell(-1)
                            newModalCell.innerHTML = `<a href="/movie/id">${movie[key]}</a>`
                        }
                    }
                })
                .then((movies) => {
                    $("#myModal").modal()
                })
        })
    }
}


// async function modalInserting (movies, url) {
//
//     let movies_table = document.getElementsByClassName("modal-body")
//     console.log(movies_table)
//
//       for (let movie of movies) {
//         let newModalRow = movies_table.insertRow(-1)
//         console.log(movie)
//         let movie = await fetch(url)
//
//         for (let key in movie) {
//             let newModalCell = newModalRow.insertCell(-1)
//             newModalCell.innerText = movie[key]
//
//         }
//     }
//     $("#myModal").modal()
// }

actorsModal()