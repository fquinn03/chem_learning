$( document ).ready(function() {
  $('.mymodal').modal();
  $('.modal-content').load("{% url 'get_formula' %}");
});
