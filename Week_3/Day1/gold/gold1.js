let allBooks = [{
    title: "The Hundred-Year-Old Man",
    author: "Jonas Jonasson",
    image : 'https://images.booklooker.de/s/00p7eu/Jonas-Jonasson+Der-Hundertj%C3%A4hrige-der-aus-dem-Fenster-stieg-und-verschwand.jpg',
    alreadyRead : true
},{
    title: "In Order To Live : A North Korean Girl's Journey to Freedom",
    author: "Yeonmi Park",
    image : 'https://d1w7fb2mkkr3kw.cloudfront.net/assets/images/book/lrg/9780/2419/9780241973035.jpg',
    alreadyRead : true
}]

let listBooks = document.getElementsByClassName("listBooks")[0];

let table = document.createElement("table");
table.style.border="1px solid black";
table.style.width ="100px";
table.style.padding="16px";

const tr = document.createElement('tr');

const titelCreate = document.createElement('th');
titelCreate.textContent = 'title';


const detailCreate = document.createElement('th');
detailCreate.textContent = 'author';


const picCreate = document.createElement('th');
picCreate.textContent = 'pic';


tr.appendChild(titelCreate);
tr.appendChild(detailCreate);
tr.appendChild(picCreate);

table.appendChild(tr);
listBooks.appendChild(table);

allBooks.forEach(e => {
    const tr = document.createElement('tr');

    const titalNew = document.createElement('td');
    titalNew.textContent = e.title;

    const detailNew = document.createElement('td');
    detailNew.textContent = e.author;
    if (e.alreadyRead) detailNew.style.color = 'red';

    const pic = document.createElement('td');
    const img = document.createElement('img');
    img.src = e.image;
    img.style.width = '100px';
    pic.appendChild(img);

    tr.appendChild(titalNew);
    tr.appendChild(detailNew);
    tr.appendChild(pic);
    table.appendChild(tr);
    listBooks.appendChild(table);

});

