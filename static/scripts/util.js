function shows_sort() {
    const th = document.getElementsByTagName('th')
    console.log(th)
    for (let a = 0; a < th.length; a++) {
            // console.log(th[i].textContent)

        th[a].addEventListener('click', item(a))
    }
}

function item(a) {
    return function () {
        sortTable(a)
    }

}

function sortTable(a) { // DESCENDING
    let table, rows, switching, i, item, nextItem, shouldSwitch;
    table = document.getElementById('shows_table')
    switching = true

    while (switching) {
        switching = false
        rows = table.rows

        for (i = 1; i < rows.length; i++){
            shouldSwitch = false
            console.log(rows[i].getElementsByTagName('td')[a])

            item = rows[i].getElementsByTagName('td')[a];
            nextItem = rows[i +1].getElementsByTagName('td')[a]

            if (item.innerHTML.toLowerCase() < nextItem.innerHTML.toLowerCase()) {
                shouldSwitch = true
                break
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);

            switching = true
        }
    }
}
