let input = document.getElementById("input");

input.addEventListener("input", () => {
    let onlyNum = input.value.match(/[^a-zA-Z0-9äöüÄÖÜß]/g);
    if ( onlyNum !== null) {
        input.value = onlyNum.join("");
    }else {
        input.value = input.value.slice(0, -1)
    }
})

// input.addEventListener('input', function () {
//     const found = input.value.match(/[^a-zA-Z0-9äöüÄÖÜß]/g);
//     if (found !== null) {
//         input.value = found.join('');
//     } else {
//         input.value = input.value.slice(0, -1);
//     }
// });