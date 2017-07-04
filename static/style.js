$('.tab').click(function (event) {
  $('.tab').removeClass('active')
  $(event.currentTarget).addClass('active')
})
