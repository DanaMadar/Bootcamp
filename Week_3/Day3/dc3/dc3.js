let input = document.getElementById("input");

input.addEventListener("input", () => {
    let onlyNum = input.value.match(/^[A-Za-z]+$/);
    if ( onlyNum !== null) {
        input.value = onlyNum.join("");
    }else {
        input.value = input.value.slice(0, -1)
    }
})
