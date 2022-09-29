const completed_list = document.querySelectorAll('.completed')

for (let completed of completed_list) {
  if (completed.innerText == 'True') {
    onelineTags = completed.parentElement.children
    for (let tag of onelineTags) {
      tag.classList.add('text-decoration-line-through')
      // if (!tag.classList.contains('text-decoration-line-through')) {
      //   tag.classList.add('text-decoration-line-through')
      // }
    }
  }
}