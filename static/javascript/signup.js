var passwordOne = document.getElementById('passwordOne');
var passwordTwo = document.getElementById('passwordTwo');
var passwordCheckOne = document.getElementById('passwordCheckOne');
var passwordCheckTwo = document.getElementById('passwordCheckTwo');
var passwordCheckThree = document.getElementById('passwordCheckThree');
var passwordCheckFour = document.getElementById('passwordCheckFour');
var passwordCheckFive = document.getElementById('passwordCheckFive');
var signUpButton = document.getElementById('signUpButton');
passwordOne.addEventListener('keyup', function () {
    passwordCheck(passwordOne.value, passwordTwo.value);
});
passwordTwo.addEventListener('keyup', function () {
    passwordCheck(passwordOne.value, passwordTwo.value);
});

passwordCheck = (firstPassword, secondPassword) => {
    var strengthBar = document.getElementById('strength');
    var strength = 0;
    if (firstPassword.match(/[a-z]+/)) {
        strength += 1;
    }
    if (firstPassword.match(/[A-Z]+/)) {
        strength += 1;
    }
    if (firstPassword.match(/[!@#$%^&*()~<>\[\]\\\/?{}'";:,.=+|_-`]+/)) {
        strength += 1;
    }
    if (firstPassword.match(/[0-9]+/)) {
        strength += 1;
    }

    [];

    if (firstPassword.length > 7) {
        strength += 1;
    }
    strengthBar.value = strength * 20;
    console.log(
        `PasswordOne: ${firstPassword} and passwordTwo: ${secondPassword}`
    );
    if (strength === 0) {
        signUpButton.style.color = 'red';
        strengthBar.value = 0;
        signUpButton.style.pointerEvents = 'none';
    } else if (strength > 0 && strength < 5) {
        signUpButton.style.color = 'red';
        signUpButton.style.pointerEvents = 'none';
    } else if (strength === 5 && firstPassword === secondPassword) {
        signUpButton.style.pointerEvents = 'auto';
        signUpButton.style.color = 'green';
        passwordOne.style.backgroundColor = '#e6f2ff';
        passwordTwo.style.backgroundColor = '#e6f2ff';
    } else {
        signUpButton.style.pointerEvents = 'none';
        signUpButton.style.color = 'red';
    }
};
