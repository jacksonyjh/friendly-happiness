function clicked() {
    // let userInput = document.getElementById('user').value;

    // // alert(userInput);
    //document.getElementById('results').innerHTML = userInput;
    // `<button>click again</button>`
    //console.log('FGHJKL')
    fetch("https://949a-169-234-109-73.ngrok.io/")
        .then(res => res.json())
        .then(response => {
            console.log(response);
            // response.data.forEach(sport => {
                // document.getElementById('results').innerHTML += `<img src="${sport.relationships.images.data?.[0].url}" />`;

            document.getElementById('results').innerHTML += response.data[0].attributes.name;

            // i = 0
            // while (i < response.data.length) {
            //     document.getElementById(
            //         'results'
            //     ).innerHTML += response.data[i].attributes.name + "<br />";
            //     i += 1
            // }
            //document.getElementById(
                //'results'
            //).innerHTML += `<img src="${response.data[0].attributes.icon}" />`;
            //document.getElementById(
                //'results'
           //).innerHTML += (response.data[0].attributes.name)
        });
}

function search() {
    let userInput = document.getElementById('user').value;

    // // alert(userInput);
    //let x = document.getElementById('results');
    // `<button>click again</button>`
    //console.log('FGHJKL')
    fetch("https://2e3e-169-234-109-73.ngrok.io/")
        .then(res => res.json())
        .then(response => {
            console.log(response);
            // response.data.forEach(sport => {
                // document.getElementById('results').innerHTML += `<img src="${sport.relationships.images.data?.[0].url}" />`;

            //document.getElementById('results').innerHTML += response.data[0].attributes.name;
            //let x = document.getElementById('results');
            for (i = 0; i < response.data.length; i++) {
                if (response.data[i].attributes.name.includes(userInput) || userInput.includes(response.data[i].attributes.name)) {
                    document.getElementById(
                        'results'
                    ).innerHTML += response.data[i].attributes.name + "<br />";
                }
            }
            // i = 0
            // while (i < response.data.length) {
            //     document.getElementById(
            //         'results'
            //     ).innerHTML += response.data[i].attributes.name + "<br />";
            //     i += 1
            // }
            //document.getElementById(
                //'results'
            //).innerHTML += `<img src="${response.data[0].attributes.icon}" />`;
            //document.getElementById(
                //'results'
           //).innerHTML += (response.data[0].attributes.name)
        });
}
