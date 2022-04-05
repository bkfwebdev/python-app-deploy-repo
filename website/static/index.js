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
console.log("datanodes",dataNodes);
dataNodes.forEach(dataNode => {
    /* if(!element){return} */
    if(dataNode.nodeType == 1){
    if (dataNode.className == "name"){formData.append("RestaurauntName",dataNode.textContent)}
    if (dataNode.className == "phone"){formData.append("PhoneNumber",dataNode.textContent)}
    if (dataNode.className == "website"){formData.append("Website",dataNode.textContent)}
    if (dataNode.className == "address"){formData.append("StreetAddress",dataNode.textContent)}
    }   
});

console.log(formData)
fetch("/",
    {
        body: formData,
        method: "POST"
    });
li.remove();
console.log("function complete")
}

function eventCaptureTest(){
    alert("event captured")
}