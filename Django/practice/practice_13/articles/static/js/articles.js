const comment_content = document.querySelector('#id_content')
const is_anonymous = document.querySelector('#is_anonymous')

if (is_anonymous.defaultValue == 'True') {
  comment_content.setAttribute('disabled', 'True')
}