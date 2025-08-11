document.addEventListener("DOMContentLoaded", function () {
    const commentForm = document.getElementById("comment-form");

    if (commentForm) {
        commentForm.addEventListener("submit", function (e) {
            e.preventDefault();

            const formData = new FormData(commentForm);
            fetch(commentForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const commentBox = document.getElementById("comment-box");
                    const newComment = document.createElement("div");
                    newComment.innerHTML = `<strong>${data.user}</strong>: ${data.comment}`;
                    commentBox.appendChild(newComment);
                    commentForm.reset();
                } else {
                    alert("Comment failed!");
                }
            });
        });
    }
});
