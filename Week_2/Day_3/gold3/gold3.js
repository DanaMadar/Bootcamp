let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}
coun= 0;

while (count< 6) {
    count += 1;
    console.log(building[numberLevels]);
}