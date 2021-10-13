const input = prompt('Please enter a list of words separated by commas');
const list = input.split(',').map(e => e.trim());
let longest = 0;
list.forEach(e => {
    if (e.length > longest) longest = e.length;
})

console.log('*'.repeat(longest + 4));
list.forEach(e => console.log(`* ${e}${' '.repeat(longest - e.length)} *`))
console.log('*'.repeat(longest + 4));