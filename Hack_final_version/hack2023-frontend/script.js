function clicked() {
    let userInput = document.getElementById('user').value;
    // alert(userInput);
    //document.getElementById(
        //'results'
    //).innerHTML = userInput;
    // `<button>click again</button>`

    fetch('http://127.0.0.1:5000')
        .then(res => res.json())
        .then(response => {
            console.log(response);
            i = 0
            while (i < response.data.length) {
                document.getElementById(
                    'results'
                ).innerHTML += response.data[i].attributes.name + "<br />";
                i += 1
            }
            //document.getElementById(
                //'results'
            //).innerHTML += `<img src="${response.data[0].attributes.icon}" />`;
            //document.getElementById(
                //'results'
           //).innerHTML += (response.data[0].attributes.name)
        });
}