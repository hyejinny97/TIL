// accounts/follower.html
// 팔로우 비동기 처리
const followerFollowForms = document.querySelectorAll('.follower-follow-form')
const followerPageCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

followerFollowForms.forEach((followerFollowForm) => {
  followerFollowForm.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
      method: 'post',
      url: `/accounts/${followerFollowForm.dataset.userPk}/follow/`,
      headers: { 'X-CSRFToken': followerPageCsrftoken },
    }).then(function (response) {
      // 팔로우 버튼 없애기
      followerFollowForm.style.display = 'none'
    })
  })
})