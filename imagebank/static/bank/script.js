const thFile = document.getElementById("id_image");
thFile.addEventListener("change", changelabel, false);
function changelabel(){
    var Filelabel = document.getElementsByClassName("custom-file-label")[0];
    Filelabel.textContent = thFile.files[0].name;
}   

function clear(){
    document.getElementsByTagName("label")[0].textContent = "";
    document.getElementsByTagName("textarea")[0].textContent = "";
}