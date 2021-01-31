
//Exercise Hangman Game


let word = prompt("Choose a word to guess");
let answerArr = [];


function startGame() {

    for (var i = 0; i < word.length; i++) {
        if (word.length > 8) {
            answerArr[i] = "*";
        }
        else {
            alert("Your word must contain 8 entry");
            return
        }

    }

    var remainingLetters = word.length;

    while (remainingLetters > 0) {
        alert(answerArr.join(" "));
        var guess = prompt("Guess a letter, or click cancel to stop playing.");
        if (guess === null) {
            break;
        } else if (guess.length !== 1) {
            alert("Please enter a single letter.");
        } else {


            for (var j = 0; j < word.length; j++) {
                if (word[j] === guess) {
                    answerArr[j] = guess;
                    remainingLetters--;
                }
            }
        }
    }

    alert(answerArr.join(" "));
    alert("Good job! The answer was " + word);
}

startGame();