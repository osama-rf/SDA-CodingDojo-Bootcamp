/*
Array: Concat
.push allowed: arrName.push(newItem)
Replicate JavaScript’s concat() which combines two arrays into one NEW array
Input: two arrays
Output: one NEW array with the items of both in the original order
*/

const arrA1 = ["a", "b"]
const arrB1 = [1, 2, 3]
// const expected1 = ["a", "b", 1, 2, 3]

// const arrA2 = [1, 2, 3]
// const arrB2 = ["a", "b"]
// const expected2 = [1, 2, 3, "a", "b"]

    // function concat(arr1, arr2) {
    //     for(var i=0; i< arr2.length; i++) {
    //         arr1.push(arr2[i]);
    //     }
    //     return arr1
    // }
    // console.log(concat(arrA1, arrB1))

    var x = "hygtfrf";
    var y ="766563";
    
    const  arr11 = [...x,...y]

    console.log(arr11)

// const arrA1 = ["a", "b"]
// const arrB1 = [1, 2, 3]
// concat(arrA1, arrB1)

/* ******************************************************************************** */
// Interview 2020!!
/*
Given one array,
return a new array that contains all of the original items duplicated twice
*/

const arr1 = ["a", "b", "c"];
const expected1 = ["a", "b", "c", "a", "b", "c"];

const arr2 = ["a"];
const expected2 = ["a", "a"];

const arr3 = [];
const expected3 = [];

function concatArrWithSelf(arr) {
    var newArr = []
    var repeat = 2  
    for (var i=1; i<=repeat; i++) {
        for(var j=0; j<arr.length; j++) {
            newArr.push(arr[j])
        }
    }
    return newArr
}
console.log(concatArrWithSelf(arr1))
  // const arrA3 = ["a", "b"]
  // console.log(concatArrWithSelf(arrA3))