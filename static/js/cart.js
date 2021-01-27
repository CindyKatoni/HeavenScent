var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',
            productId, 'action:', action)

        console.log('USER:', user)
        if (user === "AnonymousUser") {
            console.log("Not logged in")
        } else {
            updateUserOrder(productId, action)
                // console.log("User is logged in. Sending data...")
        }
    })
}

function updateUserOrder(productId, action) {
    console.log("User is authenticated. Sending data...")

    //Send the data using fetch api
    var url = '/update_item/' //this is the url we want to send the data to
}