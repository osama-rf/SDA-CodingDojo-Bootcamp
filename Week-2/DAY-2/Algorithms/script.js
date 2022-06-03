
/*
Given an array, reverse it's items in place
return the array after reversing it
Do it in place without using any built in methods
*/

const arr1 = [1, 2, 3]
const expected1 = [3, 2, 1]

// const arr2 = ["a", "b"]
// const expected2 = ["b", "a"]

// const arr3 = ["a"]
// const expected3 = ["a"]

// const arr4 = []
// const expected4 = []


function reverseArr(arr) {
    for (var i = 0; i < arr.length / 2; i++) {
        var x = arr[i];

        arr[i] = arr[arr.length - 1 - i];
        arr[arr.length - 1 - i] = x;
    }
    return arr
}

console.log(reverseArr(arr1))
console.log(reverseArr(arr2))


  // reverseArr([1, 2, 3, 4, 5])