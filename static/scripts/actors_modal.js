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
                    for (let movie of movies) {
                        let newModalRow = movies_table.insertRow(-1)
                        let newModalCell = newModalRow.insertCell(-1)

                        newModalCell.innerHTML = `<a href="/movie/${movie['id']}">${movie['title']}</a>`
                    }

                    $("#myModal").modal()
                })
                .catch(error => alert(error.message));
        })
    }
}

actorsModal()