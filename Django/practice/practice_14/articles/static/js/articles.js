// articles/detail.html
// article 좋아요 비동기 처리
const likeForm = document.querySelector('#article-like-form');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

likeForm.addEventListener('submit', function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `/articles/${likeForm.dataset.articlePk}/like/`,
    headers: { 'X-CSRFToken': csrftoken },
  }).then(function (response) {
    // 좋아요 아이콘 토글
    // const thumbUp = document.querySelector('#detail-thumbs-up')
    const thumbUp = document.querySelector('#article-like-form > button > i')
    thumbUp.classList.toggle('fa-solid')
    thumbUp.classList.toggle('fa-regular')
    thumbUp.classList.toggle('text-primary')
    // if (response.data.is_liked === false) {
    //   thumbUp.classList.remove('fa-solid')
    //   thumbUp.classList.add('fa-regular')
    //   thumbUp.classList.remove('text-primary')
    // } else {
    //   thumbUp.classList.remove('fa-regular')
    //   thumbUp.classList.add('fa-solid')
    //   thumbUp.classList.add('text-primary')
    // }

    // 좋아요 수 변경
    // const articleLikeCnt = document.querySelector('#article-like-users-cnt')
    const articleLikeCnt = document.querySelector('#article-like-form > button > span')
    articleLikeCnt.innerText = response.data.article_like_cnt
    articleLikeCnt.classList.toggle('text-primary')
  })
})

// comment 좋아요 비동기 처리
const commentLikeForms = document.querySelectorAll('.comment-like-form')

commentLikeForms.forEach((commentLikeForm) => {
  commentLikeForm.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
      method: 'post',
      url: `/articles/${commentLikeForm.dataset.articlePk}/comments/${commentLikeForm.dataset.commentPk}/like/`,
      headers: { 'X-CSRFToken': csrftoken },
    }).then(function (response) {
      // 좋아요 버튼 토글
      const thumbUp = document.querySelector('.comment-like-form > button > i')
      thumbUp.classList.toggle('fa-solid')
      thumbUp.classList.toggle('fa-regular')
      thumbUp.classList.toggle('text-primary')

      // 좋아요 수 변경
      const commentLikeCnt = document.querySelector('.comment-like-form > button > span')
      commentLikeCnt.innerText = response.data.comment_likes_cnt
      commentLikeCnt.classList.toggle('text-primary')
    })
  })
})