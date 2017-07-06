$('.tab').click(function (event) {
  $('.tab').removeClass('active')
  $(event.currentTarget).addClass('active')
})

$('.modal').click(function () {
  if (event.target.className == 'modal-content-wrapper') {
    $(event.target).parent().remove()
  }
})

$(document).ready(function () {
  if (Cookies.get("wwm-user") == null || Cookies.get("wwm-user").length == 0) {
    $('#wwm-name-modal').removeClass("hide")
  }
})

$('#wwm-name-button').click(function () {
  var user = $("#wwm-name").val()
  if (user.length > 0) {
    Cookies.set("wwm-user", user)
    $('#wwm-name-modal').remove()
  }
})
