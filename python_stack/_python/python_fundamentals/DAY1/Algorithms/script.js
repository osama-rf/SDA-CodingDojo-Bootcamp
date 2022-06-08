/*
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

// const str1 = "creature"
// const expected1 = "erutaerc"

// const str2 = "dog"
// const expected2 = "god"

function reverseString(str) {
    var len = ""
    for (var i = str.length - 1; i >= 0; i--) {
        len += str[i];
    }
    return len;
}
// console.log(reverseString(str1))
// console.log(reverseString(str2))



/*****************************************************************************/

/*
    Acronyms
  
    Create a function that, given a string, returns the string’s acronym
    (first letter of each word capitalized).
  
    Do it with .split first if you need to, then try to do it without
  */

const str1 = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";

// const str2 = "Live from New York, it's Saturday Night!";
// const expected2 = "LFNYISN";

function acronymize(str) {
    var array = str.split(" ");
    var words = ""
    for (var i = 0; i < array.length; i++) {
        if (array[i][0] == undefined){
            continue;
        }else {
            words += array[i][0];
        }
    }
    return words.toUpperCase()
}

console.log(acronymize(str1))

/*****************************************************************************/

/* case insensitive string compare */

//   const strA1 = "ABC";
//   const strB1 = "abc";
//   const expected1 = true;

//   const strA2 = "ABC";
//   const strB2 = "abd";
//   const expected2 = false;

//   const strA3 = "ABC";
//   const strB3 = "bc";
//   const expected3 = false;

function caseInsensitiveStringCompare(strA, strB) {
    // code here
}