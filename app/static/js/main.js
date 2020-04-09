
$(document).ready(function() {
    // Открывается поп-ап регистрации
    let topNav = document.querySelector('#topNav');
    let loginPopup = document.getElementById('loginPopup');
    let exitPopup = document.getElementsByClassName('exit')[0];

    topNav.addEventListener('click', ()=> {
        let target = event.target
        if (target.id == 'logIn' || target.id == 'reg') {
            loginPopup.classList.add('active')
        }
    })

    // exitPopup.addEventListener('click', ()=> {
    //     loginPopup.classList.remove('active')
    // })

    loginPopup.addEventListener('click', ()=> {
        loginPopup.classList.remove('active')
    })

    $('form').click(function (event) {
        event.stopPropagation()
    })


});