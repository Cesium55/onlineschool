const signInBtn = document.querySelector('.signin-btn');
const signUpBtn = document.querySelector('.signup-btn');
const formBox = document.querySelector('.form-box');
const body = document.body;

signUpBtn.addEventListener('click', function(){
    formBox.classList.add('active');
    body.classList.add('active');
});

signInBtn.addEventListener('click', function(){
    formBox.classList.remove('active');
    body.classList.remove('active');
});

//вход

const form = document.querySelector('.form__signin');
const emailInput = form.querySelector('.form__email__signin');
const passwordInput = form.querySelector('.form__password__signin');
const submitBtn = form.querySelector('.form__btn__signin');


form.addEventListener('submit', function(e) {
    //e.preventDefault();
    
    if(validateEmail(emailInput.value) && validatePassword(passwordInput.value.length)) {
        alert('Форма заполнена правильно!');
        form.submit();
    }
});

emailInput.addEventListener('input', function() {
    if(!validateEmail(emailInput.value)) {
        emailInput.classList.add('is-invalid');
        highlightFieldRed(emailInput)
    } else {
        emailInput.classList.remove('is-invalid');
        highlightFieldGreen(emailInput)
    }
});

passwordInput.addEventListener('input', function() {
    if(!validatePassword(passwordInput.value.length)) {
        passwordInput.classList.add('is-invalid');
        highlightFieldRed(passwordInput)
    } else {
        passwordInput.classList.remove('is-invalid');
        highlightFieldGreen(passwordInput)
    }
});

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validatePassword(password) {
    const passwordMinLength = 6;
    const passwordMaxLength = 20;
    return password>passwordMinLength && password<passwordMaxLength;
}


//регистрация


const formUp = document.querySelector('.form__signup');
const emailInputUp = form.querySelector('.form__email__signup');
const passwordInputUp = form.querySelector('.form__password__signup');
const confirmPassword = form.querySelector('.form__confpassword__signup');
const submitBtnUp = form.querySelector('.form__btn__signup');

formUp.addEventListener('submit', function(e) {
    //e.preventDefault();
    alert('Форма заполнена правильно!');
    formUp.submit();
    // if(validateEmail(emailInputUp.value) && validatePassword(passwordInputUp.value.length) && validateConfirmPassword(confirmPassword.value, passwordInputUp.value)) {
    //     alert('Форма заполнена правильно!');
    //     formUp.submit();
    // }
});

emailInputUp.addEventListener('input', function() {
    if(!validateEmail(emailInputUp.value)) {
        emailInputUp.classList.add('is-invalid');
        highlightFieldRed(emailInputUp)
    } else {
        emailInputUp.classList.remove('is-invalid');
        highlightFieldGreen(emailInputUp)
    }
});

passwordInputUp.addEventListener('input', function() {
    if(!validatePassword(passwordInputUp.value.length)) {
        passwordInputUp.classList.add('is-invalid');
        highlightFieldRed(passwordInputUp)
    } else {
        passwordInputUp.classList.remove('is-invalid');
        highlightFieldGreen(passwordInputUp)
    }
});

confirmPassword.addEventListener('input', function() {
    if(!validateConfirmPassword(confirmPassword.value, passwordInputUp.value)) {
        confirmPassword.classList.add('is-invalid');
        highlightFieldRed(confirmPassword)
    } else {
        confirmPassword.classList.remove('is-invalid');
        highlightFieldGreen(confirmPassword)
    }
});

function validateConfirmPassword(firstPassword, secondPassword) {
    return firstPassword == secondPassword;
}

function highlightFieldRed(field) {
    field.style.backgroundColor  = 'lightcoral';
}

function highlightFieldGreen(field) {
    field.style.backgroundColor  = 'lightgreen';
}

