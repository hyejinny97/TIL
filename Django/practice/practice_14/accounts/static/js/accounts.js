// accounts/detail.html
// 팔로우 비동기 처리
const followForm = document.querySelector('.detail-follow-form')
const detailPageCsrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

followForm.addEventListener('submit', function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `/accounts/${followForm.dataset.userPk}/follow/`,
    headers: { 'X-CSRFToken': detailPageCsrftoken },
  }).then(function (response) {
    // 팔로우 버튼 토글
    const followBtn = document.querySelector('.detail-follow-form > input[type=submit]')

    if (response.data.is_followed === false) {
      followBtn.value = '팔로우'
    } else {
      followBtn.value = '팔로우 취소'
    }

    // 팔로우/팔로워 수 변경
    const followingCnt = document.querySelector('.following-cnt')
    const followerCnt = document.querySelector('.follower-cnt')

    followingCnt.innerText = response.data.following_cnt
    followerCnt.innerText = response.data.follower_cnt
  })
})

