let arr = ["apple", "banana", "cherry", "date", "elder"]
let arr2 = []

for (let x = 0; x < arr.length; x++) {
    for (let y = 0; y < arr[x].length; y++) {
        if (arr[x][y] == "a") {
            if (arr[x] == arr2[x]) {
                continue
            }
            else {
                arr2.push(arr[x])
            }
        }
    }
}

for (let i = 0; i < arr2.length; i++) {
    console.log(arr2[i]);
}

// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
// }
