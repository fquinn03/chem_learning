$(document).ready(function(){

  $('#convert').click(function() {
    var output = document.getElementById("formula_output")
    output.innerHTML=""
    var input = document.getElementById('formula_input')
    raw_formula = input.value;
    output.innerHTML += "<p>$$\\ce{"+ raw_formula +"}$$</p>"
    MathJax.Hub.Queue(["Typeset",MathJax.Hub,"formula_output"]);
  })
})
