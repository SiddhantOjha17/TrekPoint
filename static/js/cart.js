var updateBtns = document.getElementsByClassName("update-cart")

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)
        console.log("User: ", user)

        updateUserOrder(productId, action)

    })
}

function updateUserOrder(productId, action) {
    console.log('User is Logged In, Sending data ... ')

    var url = "update_item/"
    console.log(productId)

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            // 'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, "action": action})
    })

    .then((response) => {
        console.log("in first promise")
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}
