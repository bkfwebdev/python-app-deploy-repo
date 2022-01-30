function deleteNote(noteId){
    fetch('/delete-note',{
        method:'POST',
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res)=>{
        window.location.href = "/";
    });
}

/*
additional functions or modifications needed
add favorite
delete favorite
*/