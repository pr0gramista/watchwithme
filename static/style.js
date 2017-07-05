$('.tab').click(function (event) {
  $('.tab').removeClass('active')
  $(event.currentTarget).addClass('active')
})

$('.modal').click(function () {
  console.log(event);
  if (event.target.className == 'modal-content-wrapper') {
    $(event.target).parent().remove()
  }
})

$('#wwm-name-button').click(function () {
  var user = $("#wwm-name").val()
  if (user.length > 0) {
    Cookies.set("wwm-user", user)
    $('#wwm-name-modal').remove()
  }
})
