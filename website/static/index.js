function deleteFavorite(favoriteId){
    fetch('/delete-favorite',{
        method:'POST',
        body: JSON.stringify({ favoriteId: favoriteId}),
    }).then((_res)=>{
        window.location.href = "/";
    });
}

