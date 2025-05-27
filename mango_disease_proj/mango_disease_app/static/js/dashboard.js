function orchardTab(evt, id) {
    document.querySelectorAll(".tabcontent") 
        .forEach(el => el.style.display = "none"); //Hide Contents

    document.querySelectorAll(".tablink")
        .forEach(btn => btn.classList.remove("active")); //Deactive buttons

    document.getElementById(id).style.display = "block";  //Show on CLick
    evt.currentTarget.classList.add("active");

    const firstCaseBtn = document.querySelector(`#${id} .caselink`); //Auto select first case
    if (firstCaseBtn) firstCaseBtn.click();
}

function caseTab(evt, id){ 
    const orchardPane = evt.currentTarget.closest(".tabcontent"); //Alightment

    orchardPane.querySelectorAll(".casecontent")
             .forEach(el => el.style.display = "none"); //Hide Contents

    orchardPane.querySelectorAll(".caselink")
             .forEach(btn => btn.classList.remove("active")); //Deactive buttons

    document.getElementById(id).style.display = "block"; //Show on CLick
    evt.currentTarget.classList.add("active");
}


document.addEventListener("DOMContentLoaded", () => {   //Show first orchard dashboard one exists
    const firstOrchardBtn  = document.querySelector(".tablink");
    if (firstOrchardBtn) firstOrchardBtn.click();
});