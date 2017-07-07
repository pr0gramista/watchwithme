function get_user() {
  var user = Cookies.get('wwm-user')
  if (user == null || user.length == 0) {
    user = "Anonymous"
  }
  return user
}

function get_secret() {
  return Cookies.get('wwm-secret')
}
