const btns = document.querySelectorAll("[data-target]");
const close_btns = document.querySelectorAll(".modal-btn");
const overlay = document.querySelector("#overlay");
const body = document.querySelector("body");


btns.forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelector(btn.dataset.target).classList.add("active");
        overlay.classList.add("active");
        body.classList.add("active");
    })
})

close_btns.forEach(btn => {
    btn.addEventListener('click', () => {
        const modals = document.querySelectorAll(".modal");
        modals.forEach((modal) => modal.classList.remove("active"));
        overlay.classList.remove("active");
        body.classList.remove("active");
    })
})

window.onclick = (e) => {
    if (e.target == overlay) {
        const modals = document.querySelectorAll(".modal");
        modals.forEach((modal) => modal.classList.remove("active"));
        overlay.classList.remove("active");
        body.classList.remove("active");
    }
}

console.log("JS is connected")