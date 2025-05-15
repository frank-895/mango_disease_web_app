function orchardTab(evt, id) {
document.querySelectorAll(".tabcontent") 
    .forEach(el => el.style.display = "none"); //Hide Contents

document.querySelectorAll(".tablink")
    .forEach(btn => btn.classList.remove("active")); //Deactive buttons

document.getElementById(id).style.display = "block";  //Show on CLick

evt.currentTarget.classList.add("active");    //Activate this button
}

document.addEventListener("DOMContentLoaded", () => {   //Show first orchard dashboard if it exists
    const firstBtn = document.querySelector(".tablink");
    if (firstBtn) firstBtn.click();
});