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
      const thumbUp = document.querySelector(`#comment-${commentLikeForm.dataset.commentPk}-like > button > i`)
      thumbUp.classList.toggle('fa-solid')
      thumbUp.classList.toggle('fa-regular')
      thumbUp.classList.toggle('text-primary')

      // 좋아요 수 변경
      const commentLikeCnt = document.querySelector(`#comment-${commentLikeForm.dataset.commentPk}-like > button > span`)
      commentLikeCnt.innerText = response.data.comment_likes_cnt
      commentLikeCnt.classList.toggle('text-primary')
    })
  })
})

// 댓글 작성 비동기 처리
const commentCreateForm = document.querySelector('.detail-comment-create-form')

commentCreateForm.addEventListener('submit', function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `/articles/${commentCreateForm.dataset.articlePk}/comments/create/`,
    headers: { 'X-CSRFToken': csrftoken },
    data: new FormData(commentCreateForm)
  }).then(function (response) {
    // 기존 댓글 모두 삭제
    const commentsDivTag = document.querySelector('#comments')
    const originalComments = document.querySelectorAll('#comments > section')
    for (let originalComment of originalComments) {
      commentsDivTag.removeChild(originalComment)
    }

    // 모든 댓글 추가
    const comments = response.data.comments
    for (let comment of comments) {
      const commentBlock = document.createElement('section')
      commentBlock.classList.add('d-flex', 'p-2', 'mt-3')

      const contentTag = document.createElement('p')
      contentTag.innerText = `${comment.writer_username} | ${comment.content}`

      commentBlock.appendChild(contentTag)

      commentsDivTag.appendChild(commentBlock)
    }

    // 댓글 폼에 있는 content 삭제
    commentCreateForm.reset()
  })
})


// 댓글 삭제 비동기 처리
const commentDeleteForms = document.querySelectorAll('.detail-comment-delete-form')

commentDeleteForms.forEach((commentDeleteForm) => {
  commentDeleteForm.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
      method: 'post',
      url: `/articles/${commentDeleteForm.dataset.articlePk}/comments/${commentDeleteForm.dataset.commentPk}/delete/`,
      headers: { 'X-CSRFToken': csrftoken },
    }).then(function (response) {
      const commentBlock = document.querySelector(`#comment-${response.data.comment_pk}-block`)
      console.log(response.data.comment_pk)
      console.log(commentBlock)
      commentBlock.classList.add('d-none')
    })
  })
})