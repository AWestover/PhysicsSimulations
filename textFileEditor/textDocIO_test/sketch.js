//Coded by Alek Westover

var doc = "";

function preload() {
  doc = loadStrings("IOData/input1.txt");
}

function setup() {
  noCanvas();
  console.log("Loaded");
}

function fetchInputDoc() {
  var full_doc = "";
  for (var i = 0; i < doc.length; i++) {
    full_doc += doc[i];
  }
  var inDocWords = split(full_doc, " ");
  var nextWord = inDocWords[round(random()*(inDocWords.length-1))];
  console.log(nextWord);
  document.getElementById("input_file_word").innerHTML = nextWord;

}

function pushInputDoc() {
 var docOut = document.getElementById("user_text_input").value;
  console.log(docOut);
  saveStrings(docOut, "p5jsoutput.txt");
}
