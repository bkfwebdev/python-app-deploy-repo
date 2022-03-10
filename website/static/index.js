function deleteFavorite(favoriteId){
    fetch('/delete-favorite',{
        method:'POST',
        body: JSON.stringify({ favoriteId: favoriteId}),
    }).then((_res)=>{
        window.location.href = "/";
    });
}

function AddNewFavorite(e){
/*get data from clicked li element*/
console.log("attempting post request")

let li = e.target.closest('li');
let dataNodes = li.childNodes;
let formData = new FormData();
dataNodes.forEach(element => {
    if (element.nextElementSibling.className = "name"){formData.append("RestaurauntName",element.textContent)}
    if (element.nextElementSibling.className = "phone"){formData.append("PhoneNumber",element.textContent)}
    if (element.nextElementSibling.className = "website"){formData.append("Website",element.textContent)}
    if (element.nextElementSibling.className = "address"){formData.append("StreetAddress",element.textContent)}   
});
console.log(formData)
fetch("/",
    {
        body: formData,
        method: "POST"
    });

console.log("function complete")
}

function eventCaptureTest(){
    alert("event captured")
}

/*submit data for new favorite to data base


formData.append("username", "Groucho");
formData.append("accountnum", 123456); // number 123456 is immediately converted to a string "123456"

// HTML file input, chosen by user
formData.append("userfile", fileInputElement.files[0]);

// JavaScript file-like object
var content = '<a id="a"><b id="b">hey!</b></a>'; // the body of the new file...
var blob = new Blob([content], { type: "text/xml"});

formData.append("webmasterfile", blob);

var request = new XMLHttpRequest();
request.open("POST", "http://foo.com/submitform.php");
request.send(formData);
}


*/