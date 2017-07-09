$('.tab').click(function (event) {
  $('.tab').removeClass('active')
  $(event.currentTarget).addClass('active')

  $('.tab-content').removeClass('active')
  $('#' + event.currentTarget.id + '-content').addClass('active')
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

$('#wwm-name').keypress(function (e) {
  if (e.which == 13) {
    var user = $("#wwm-name").val()
    if (user.length > 0) {
      Cookies.set("wwm-user", user)
      $('#wwm-name-modal').remove()
    }
    return false;
  }
});

$('#wwm-name-button').click(function () {
  var user = $("#wwm-name").val()
  if (user.length > 0) {
    Cookies.set("wwm-user", user)
    $('#wwm-name-modal').remove()
  }
})

$('#wwm-name-cancel').click(function () {
  Cookies.set("wwm-user", "Anonymous")
  $('#wwm-name-modal').remove()
})
