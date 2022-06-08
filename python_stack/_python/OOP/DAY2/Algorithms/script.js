/*
Given an arr and a separator string, output a string of every item in the array separated by the separator.
No trailing separator at the end
Bonus: Default the separator to a comma with a space after it if no separator is provided
*/

// const arr1 = [1, 2, 3]
// const separator1 = ", "
// const expected1 = "1, 2, 3"

// const arr2 = [1, 2, 3]
// const separator2 = "-"
// const expected2 = "1-2-3"

// const arr3 = [1, 2, 3]
// const separator3 = " - "
// const expected3 = "1 - 2 - 3"

// const arr4 = [1]
// const separator4 = ", "
// const expected4 = "1"

// const arr5 = []
// const separator5 = ", "
// const expected5 = ""

// const arr6 = [1, 2, 3]
// separator is not given
// const expected 6 = "1, 2, 3"
// function join(arr, separator) {
//     var arr = ""
//     for (var i = 0 ; i < arr.length; i++){
//         if 
//     }
// }
/*****************************************************************************/

/*
    Book Index

    Given an array of ints representing page numbers
    return a string with the page numbers formatted as page ranges when the nums span a consecutive range
  */

const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const expected1 = "1, 13-15, 37-38, 70";

function bookIndex(pageNums) {
    if(pageNums.length == 0){
        return ""
    }
    var string =""
    for (var i=0; i<pageNums.length-1; i++){
        if(pageNums[i+1] == pageNums[i]+1){
            if(pageNums[i]-1 != pageNums[i-1]){
                string+=pageNums[i]
                string+="-"
            }
        }
        else{
            string+=pageNums[i]
            string+=", "
        }
    }
    string+=pageNums[pageNums.length-1]
    return string
}

console.log(bookIndex(nums1))