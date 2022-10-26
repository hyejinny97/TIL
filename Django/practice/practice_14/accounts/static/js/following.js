// accounts/following.html
// 팔로우 비동기 처리
const followingFollowForms = document.querySelectorAll('.following-follow-form')
const followingPageCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

followingFollowForms.forEach((followingFollowForm) => {
  followingFollowForm.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
      method: 'post',
      url: `/accounts/${followingFollowForm.dataset.userPk}/follow/`,
      headers: { 'X-CSRFToken': followingPageCsrftoken },
    }).then(function (response) {
      // 팔로우 버튼 없애기
      followingFollowForm.style.display = 'none'
    })
  })
})